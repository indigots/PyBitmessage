from class_addressGenerator import *
import shared
import highlevelcrypto
from addresses import *
import ConfigParser

class chatSession (object):
    hosting = False
    hostAddress = None
    openAddress = None

    def __init__ (self, inHostAddress, isHosting, myAddress):
        self.hostAddress = inHostAddress
        self.isHosting = isHosting
        status,addressVersionNumber,streamNumber,hash = decodeAddress(inHostAddress)
        self.hostAddressVersionNumber = addressVersionNumber
        self.stream = streamNumber
        self.hostAddressHash = hash
        self.nick = 'newbie1'
        self.passphrase = ''
        if isHosting:
            if addressVersionNumber == 2 or addressVersionNumber == 3 or addressVersionNumber == 4:
                # Returns a simple 32 bytes of information encoded in 64 Hex characters,
                # or null if there was an error.
                self.hostAddressPrivEncryptionKey = shared.decodeWalletImportFormat(
                    shared.config.get(inHostAddress, 'privencryptionkey')).encode('hex')
            if len(self.hostAddressPrivEncryptionKey) == 64:#It is 32 bytes encoded as 64 hex characters
                self.hostAddressCryptor = highlevelcrypto.makeCryptor(self.hostAddressPrivEncryptionKey)
                shared.logger.debug('Cryptor for chat host address made for address ' + inHostAddress +
                    ' and hash ' + self.hostAddressHash.encode('hex'))
            else:
                shared.logger.error('Failed to create chat, could not find priv key and make decryptor.')
                return
            self.generateNewOpenAddress()
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
            self.generateNewOpenAddress()
            shared.logger.debug('Joining existing chat at ' + inHostAddress + ' using my address ' + myAddress)
            self.sendJoinMessage()

    def generateNewOpenAddress(self):
        self.openAddress,self.openAddressPrivSigningKey,self.openAddressPubSigningKey,self.openAddressPrivEncryptionKey,openAddressPubEncryptionKey = createThrowawayAddress(4, self.stream)
        shared.logger.debug('Open chat address returned ' + str(self.openAddress))

    def sendJoinMessage(self):
        shared.logger.debug('Creating join message to send to ' + self.hostAddress)
        shared.workerQueue.put(('joinChat', self))
