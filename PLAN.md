Bitmessage Moderated Chat
==========

## Overview

* A chat channel is hosted by a master address. The hoster or server user provides a normal address and keeps the private key private. This address is used as a control channel for users to make system commands to the chat channel.
  * This master address accepts control messages. This includes commands to join a channel, set a nick, promote other users to moderator or give voices.
  * After sending a message to join the channel a second address is provided including its private keys, call this the open address. This is used to send messages to all users.
  * The master disseminates status updates for the channel via the open address. This includes a list of addresses (users) that are allowed to speak, lists of users in the channel, and status changes of users.
* Messages sent on the open address must be signed by a user with the proper rights or they will be ignored. For example status updates would need to be signed by the master address. Regular chat would need to be signed by an address with chat privileges.
* Joining a channel is done using a message including a significant pow. This is to avoid banned users to easily rejoin. Or is there any point if the open address is out there?
* Messages are sent as special objects with a short TTL so they will need minimal pow work to send.
* The open address must change to a new one when a user is kicked.

## Example Message Flow
----------
1. User knows the master address of the channel they want to join.
2. User sends a join message to the master address. This would include:
  * Their personal address they are joining with.
  * The nick they want to use.
  * The passphrase if the channel is private.
  * Pow to prevent brute forcing.
3. The chat host sends back a control message to the users address. This message comes from the master address of the channel. It contains a standard status update that includes:
  * The open address of the channel including the private keys.
  * The users list:
    * Personal addresses
    * Their nicks
    * An indication of their status in the channel, has voice, is moderator etc.
4. The user now listens using the open address for chat messages and status updates.
5. When a chat message is recieved on the open address the user checks to see if the sender has a voice otherwise it is ignored.
6. When a status update is recieved from the master address. The visible user list and their statuses is updated with the new status information. If a user was kicked then the open address of the channel may change.

## Message Specifications
### Control messages
* Sent from a users personal address to the master address of the server
* TTL: 5 min ?
* New object type: 6660
* Current version: 1
* Standard encrypted message
* Unencrypted message data:
  * address_version of users address
  * stream of users
  * behavior bitfield of users
  * pub sign key of users
  * pub enc key of users
  * trials of users
  * extra bytes of users
  * destination ripe of master address
  * uint32 control message type
    * join: type 1
      * varint length of nick
      * uchar nick
      * varint length of passphrase, public channels would have a phrase length of 0
      * uchar passphrase
      * pow of bytes from address version through passphrase, use master address pow params with 28 days as the ttl var, if the passphrase is empty then just pad 8 bytes
    * set user status: type 2
      * ripe of user to modify
      * uint32 status bitfield bit 0 is kbanned, bit 32 is voice, bit 31 is moderator
  * length of signature
  * signature using the users sign key that he joined with or is joining with

### Status update
* Sent from servers master address back to all users personal addresses
* TTL: 5 min ?
* New object type: 6661
* Current version: 1
* Standard encrypted message
* Unencrypted message data:
  * Ripe address of the master address it is coming from
  * Ripe of the personal address it is going to
  * address_version of open address
  * stream of open address
  * behavior bitfield of open 
  * pub sign key of open 
  * pub enc key of open 
  * nonce trials of open
  * extra bytes
  * priv sign key of open
  * priv enc key of open
  * varint of length of current subject
  * uchar subject
  * varint of length of current passphrase
  * uchar passphrase
  * varint of number of users
  * users address info, address_version through extra bytes
  * varint of length of users nick
  * uchar of users nick
  * uint32_t of users status, bit 32 is voice, bit 31 is moderator
  * ... Repeat for all users in channel ...
  * length of signature
  * signature of the message using the master address sign key

### Chat message
* Sent from user to open address for all to recieve, keep it small for fast pow
* TTL: 1 min?
* New object type: 6662
* Current version: 1
* Standard encrypted message
* Unencrypted message data
  * ripe of the senders address
  * ripe of the destination open address
  * varint message type: 
    * standard chat message is 1
  * varint length of message
  * uchar message
  * length of signature
  * signature of the message using the personal address the user is sending from
