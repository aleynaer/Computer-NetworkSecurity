# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:33:24 2021

@author: Aleyna ER
"""
import pyDHE 

"""
kütüphane gereksinimi cli'de pip install pyDHE ile sağlanabilir
"""

# alice = pyDHE.new(group=18) 
# new içine grup argümanı atılarak kullanılabilir
# grup değeri rastgeliliği sağlar, default olarak 14'tür (RFC 3526 standardı)
# grup = 14, 2048 bitlik random anahtar oluşturur (grup 18 -> 8192 bit)

aleyna = pyDHE.new()
aleynaPubKey = aleyna.getPublicKey()
print("Aleyna'nın public anahtarı:", hex(aleynaPubKey))
print("\n")


merve = pyDHE.new()
mervePubKey = merve.getPublicKey()
print("Merve'nin public anahtarı:", hex(mervePubKey))
print("\n")

print(" ***** ... açık kanal üzerinden anahtarlar takas ediliyor ... *****")
print("\n")

aleynaSharedKey = aleyna.update(mervePubKey)
print("Aleyna'nın paylaşılan anahtarı (shared key):", hex(aleynaSharedKey))
print("\n")

merveSharedKey = merve.update(aleynaPubKey)
print("Merve'nin paylaşılan anahtarı (shared key):", hex(merveSharedKey))
print("\n")

print("Paylaşılan anahtarlar aynı mı:", aleynaSharedKey == merveSharedKey)