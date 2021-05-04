# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:33:24 2021

@author: Aleyna ER
"""
#import pyDHE 

"""
kütüphane gereksinimi cli'de pip install pyDHE ile sağlanabilir
"""
import bag

# alice = pyDHE.new(group=18) 
# new içine grup argümanı atılarak kullanılabilir
# grup değeri rastgeliliği sağlar, default olarak 14'tür (RFC 3526 standardı)
# grup = 14, 2048 bitlik random anahtar oluşturur (grup 18 -> 8192 bit)

# aleyna = pyDHE.new()
# aleynaPubKey = aleyna.getPublicKey()
# print("Aleyna'nın public anahtarı:", hex(aleynaPubKey))
# print("\n")


# merve = pyDHE.new()
# mervePubKey = merve.getPublicKey()
# print("Merve'nin public anahtarı:", hex(mervePubKey))
# print("\n")

def DHEkeyCreation():
    import pyDHE
    person = pyDHE.new()
    personPubKey = person.getPublicKey()
    print("Aleyna'nın public anahtarı:", hex(personPubKey))
    pubKey = hex(personPubKey)
    return pubKey

#%%
print(" ***** ... açık kanal üzerinden anahtarlar takas ediliyor ... *****")
print("\n")


def DHkeyExchange(pubKey):
    bag.sendMail(pubKey)
    
    

#%%
# aleynaSharedKey = aleyna.update(mervePubKey)
# print("Aleyna'nın paylaşılan anahtarı (shared key):", hex(aleynaSharedKey))
# print("\n")

# merveSharedKey = merve.update(aleynaPubKey)
# print("Merve'nin paylaşılan anahtarı (shared key):", hex(merveSharedKey))
# print("\n")

# print("Paylaşılan anahtarlar aynı mı:", aleynaSharedKey == merveSharedKey)

def DHEcreateSharedKey(p1pubKey,p2pubKey): # benim anahtar ve gelen anahtar
    sharedK = p1pubKey.update(p2pubKey)
    print("paylaşılan anahtar (shared key):", hex(sharedK))
    return sharedK

#%%

dhPubKey = DHEkeyCreation()
DHkeyExchange(dhPubKey)

