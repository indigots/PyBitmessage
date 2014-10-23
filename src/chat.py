from class_addressGenerator import *
import shared
import highlevelcrypto
from addresses import *
import ConfigParser

class chatSession (object):
    hostAddress = None
    openAddress = None

    def __init__ (self, inHostAddress, isHosting, myAddress):
        self.hostAddress = inHostAddress
        self.isHosting = isHosting
        status,addressVersionNumber,streamNumber,hash = decodeAddress(inHostAddress)
        self.hostAddressVersionNumber = addressVersionNumber
        self.stream = streamNumber
        self.hostAddressHash = hash
        shared.logger.debug('****************' + str(type(hash)) + '*********************')
        self.nick = 'newbie1'
        self.passphrase = ''
        self.usersInChannel = {}
        self.subject = 'New Chat'
        self.status = 'disconnected'
        if isHosting:
            if addressVersionNumber < 4:
                logger.debug('Only v4+ addresses supported for chat.')
                return

            self.hostAddressPrivEncryptionKey = shared.decodeWalletImportFormat(
                shared.config.get(inHostAddress, 'privencryptionkey')).encode('hex')
            if len(self.hostAddressPrivEncryptionKey) == 64:#It is 32 bytes encoded as 64 hex characters
                self.hostAddressCryptor = highlevelcrypto.makeCryptor(self.hostAddressPrivEncryptionKey)
                shared.logger.debug('Cryptor for chat host address made for address ' + inHostAddress +
                    ' and hash ' + self.hostAddressHash.encode('hex'))
            else:
                shared.logger.error('Failed to create chat, could not find priv key and make decryptor.')
                return

            self.hostAddressPrivSigningKey = shared.decodeWalletImportFormat(
                shared.config.get(inHostAddress, 'privsigningkey')).encode('hex')
                
            self.hostAddressPubSigningKey = highlevelcrypto.privToPub(self.hostAddressPrivSigningKey).decode('hex')
            self.hostAddressPubEncryptionKey = highlevelcrypto.privToPub(self.hostAddressPrivEncryptionKey).decode('hex')
            self.hostAddressBitfield = '\x00\x00\x00\x01'
            self.hostAddressNonceTrials = shared.config.getint(self.hostAddress, 'noncetrialsperbyte')
            self.hostAddressExtraBytes = shared.config.getint(self.hostAddress, 'payloadlengthextrabytes')


            self.generateNewOpenAddress()
            
            shared.UISignalQueue.put(('updateChatText', 'Chat created at ' + self.hostAddress))
            self.addUser(
                self.hostAddressVersionNumber,
                self.stream,
                self.hostAddressBitfield,
                self.hostAddressPubSigningKey,
                self.hostAddressPubEncryptionKey,
                self.hostAddressNonceTrials,
                self.hostAddressExtraBytes,
                self.nick,
                '\x00\x00\x00\x07') # permissions, owner, moderator, voice
            self.status = 'hosting'
        else:
            self.myAddress = myAddress
            mystatus,myaddressVersionNumber,mystreamNumber,hash = decodeAddress(myAddress)
            self.myAddressVersionNumber = myaddressVersionNumber
            self.myAddressHash = hash
            if myaddressVersionNumber == 2 or myaddressVersionNumber == 3 or myaddressVersionNumber == 4:
                # Returns a simple 32 bytes of information encoded in 64 Hex characters,
                # or null if there was an error.
                self.myAddressPrivEncryptionKey = shared.decodeWalletImportFormat(
                    shared.config.get(myAddress, 'privencryptionkey')).encode('hex')
            if len(self.myAddressPrivEncryptionKey) == 64:#It is 32 bytes encoded as 64 hex characters
                self.myAddressCryptor = highlevelcrypto.makeCryptor(self.myAddressPrivEncryptionKey)
                shared.logger.debug('Cryptor for chat personal address made for address ' + myAddress)
            else:
                shared.logger.error('Failed to create chat, could not find priv key and make decryptor.')
                return
            shared.logger.debug('Joining existing chat at ' + inHostAddress + ' using my address ' + myAddress)
            self.sendJoinMessage()

    def generateNewOpenAddress(self):
        self.openAddress,self.openAddressPrivSigningKey,self.openAddressPubSigningKey,self.openAddressPrivEncryptionKey,self.openAddressPubEncryptionKey,self.openAddressHash = createThrowawayAddress(4, self.stream)
        self.openAddressVersionNumber = 4
        shared.logger.debug('open key' + self.openAddressPrivEncryptionKey)
        self.openAddressCryptor = highlevelcrypto.makeCryptor(self.openAddressPrivEncryptionKey)
        sha = hashlib.new('sha512')
        sha.update(self.openAddressPubSigningKey + self.openAddressPubEncryptionKey)
        ripe = hashlib.new('ripemd160')
        ripe.update(sha.digest())
        self.openAddressHash = ripe.digest()
        shared.logger.debug('Open chat address returned ' + str(self.openAddress))

    def sendJoinMessage(self):
        shared.logger.debug('Creating join message to send to ' + self.hostAddress)
        shared.workerQueue.put(('joinChat', self))
        
    def addUser(self,addressVersion,stream,bitfield,signKey,encKey,trials,extraBytes,nick,permissionBits):
        sha = hashlib.new('sha512')
        sha.update(signKey + encKey)
        ripe = hashlib.new('ripemd160')
        ripe.update(sha.digest())
        address = encodeAddress(
            addressVersion, stream, ripe.digest())
        self.usersInChannel[ripe.digest()] = (addressVersion,stream,bitfield,signKey,encKey,trials,extraBytes,nick,address,permissionBits)
        shared.logger.debug('CHAT **** User joined using address: ' + address)
        shared.UISignalQueue.put(('updateChatText', 'User joined using address: ' + address))
        shared.UISignalQueue.put(('updateChatText', str(len(self.usersInChannel)) + ' users now in channel.'))
        #shared.UISignalQueue.put(('updateChatText', str(self.usersInChannel)))
        self.sendStatusMessage(ripe.digest())
        shared.UISignalQueue.put(('updateChatUsers', self.usersInChannel))
        
    def sendStatusMessage(self, inRipe): # without ripe message is sent on open channel to everyone
        shared.workerQueue.put(('chatStatus', (self, inRipe)))
        
    def getUserByRipe(self, inRipe):
        return self.usersInChannel[inRipe]
    
    def gotStatusUpdate(self, users, openAddressTuple, subject, passphrase):
        self.usersInChannel = users
        self.openAddressVersion,self.openAddressStream,self.openAddressBitfield,self.openAddressPubSigningKey,self.openAddressPrivSigningKey,self.openAddressPubEncryptionKey,self.openAddressPrivEncryptionKey,self.openAddressTrials,self.openAddressExtraBytes,self.openAddressHash = openAddressTuple
        self.subject = subject
        self.passphrase = passphrase
        shared.UISignalQueue.put(('updateChatText', 'Got status update. ' + str(len(self.usersInChannel)) + ' users now in channel.'))
        shared.UISignalQueue.put(('updateChatText', str(self.usersInChannel)))
        shared.UISignalQueue.put(('updateChatUsers', self.usersInChannel))
