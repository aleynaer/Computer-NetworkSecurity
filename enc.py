# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:36:05 2021

@author: Asus
"""

from Crypto.Cipher import AES
import binascii, os

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    print("cipher t: ", ciphertext)
    return (ciphertext, aesCipher.nonce, authTag)
    #return ciphertext

def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

def createKey():
    secretKey = os.urandom(32)  # 256-bit random encryption key
    print("Encryption key:", binascii.hexlify(secretKey))
    return secretKey

print("\n")

# secretKey = createKey()
# msg = "messagege"
# msg = msg.encode()
# encryptedMsg = encrypt_AES_GCM(msg, secretKey)
# print("encryptedMsg", {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'aesIV': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2])
# })

# print("\n")

# decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
# print("decryptedMsg", decryptedMsg)