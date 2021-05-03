# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:54:28 2021

@author: Asus
"""
import smtplib, ssl
import os,binascii
import enc

#%%

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "buuagodev@gmail.com"   
receiver_email = "aleynaer99@gmail.com"
password = input("Type your password and press enter:")
# message = """\
# Subject: Hi there

# This message is sent from Python."""
message = input("write your message here: \n")
message = message.encode()
key = enc.createKey()
context = ssl.create_default_context()

#msg = message.encode('UTF-8')
#%%

def sendMail(message):
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
def sendSecureMail(message):
    encryptedMsg = enc.encrypt_AES_GCM(message,key)
    print(encryptedMsg)
    ciphertext = binascii.hexlify(encryptedMsg[0])
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, ciphertext)
    #print(encryptedMsg)
    return encryptedMsg

# ciphertext = binascii.hexlify(encryptedMsg[0])
# decyrpted = enc.decrypt_AES_GCM(ciphertext, key)
# print("MESAJINIZ : ... ",  decyrpted)    

    
    
#%%

x = sendSecureMail(message)


#%%

def decyrptMAIL(msg,key):
    plainText = enc.decrypt_AES_GCM(msg, key) 
    print(plainText.decode())
    
#%%

decyrptMAIL(x, key)