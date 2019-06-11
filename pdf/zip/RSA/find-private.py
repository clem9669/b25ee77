#! /usr/bin/python
# -*- coding: utf-8 -*-`

import sys
import itertools
from itertools import product

#fonction modular inverse pour calculer d

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

prime1 = '00 fb 40 dc 44 ba 03 d1 53 42 f7 59 08 e0 f9 30 05 96 64 4a de 94 68 5e 08 e2 8c 9a b1 64 0c 2f 62 c2 9a b9 a2 39 82 4b 9e be eb 76 ae 6d 87 21 a3 5e 9e d9 8d 7e 57 38 3e 59 09 34 a5 78 cd f7 2e 89 5d 5c 37 52 ea fd f6 31 cc ba d2 d9 60 e4 45 1d 67 76 d2 1f 12 9c 9d c9 b1 90 45 51 ed d2 fb dd b6 74 b4 99 fb b1 0a d9 b7 c2 be 8b 57 07 22 0a 8e 3a 36 ff 6d c1 1d 63 93 af cb 4e c0 47 9f 65 bf df e3 f0 5f 1e 98 61 45 74 ec 36 a7 a5 b1 f1 8d 3d 97 6b 5a 82 49 09 00 08 0d 9d c2 74 57 4e 30 a1 39 68 2f 22 34 71 13 aa 3b f2 20 4f 8e 10 eb d4 d0 9b cd 8c c2 53 5f 9d 71 13 0c 0f 21 b6 6e 13 39 40 d3 a6 b1 eb 74 ad dd 0a 29 14 81 b1 90 ad e0 53 f0 89 c8 00 fe dc ad 56 59 fc 28 1d c0 cf 5e 08 c0 54 33 24 a3 52 bb f3 25 10 43 c3 73 b8 40 4f fc 6b 6b 77 bd 5f 22 24 eb fb 15'

combination = {'fb':['7f','fb'],'12':['f4','12'],'54':['16','54'],'57':['a4','57'],'cd':['b5','cd']}

lst = [[word] + list(combination[word]) if word in combination else [word] for word in prime1.split()]

resultat = [''.join(line) for line in product(*lst)]
resultat2 = list(set(resultat)) #supprime les doublons

N = 0x00cd5f8a24c7605008897a3c922c0e812e769de0a46442c350cb78c7868539f3d38aac80b3e6a506605910e8599806b4d1d148f2f6b81da04796a8a5aee18f29e83e16775a2a0a00870541f6574ed1438636ae0a0c116e07104f48f72094863a3869e1c8fc220627278962fb22873e3156f18e55dec94e970064ec7f4e0e88454012e2fd5dfe5f8d19bf170f9ccb3f46e0fd1019bcb02d9083a0703c617f996379e6478354a73ae6e6acbce1f4333ecfaf24366a3e977d3cd3cbfe8d8a387bd876bfdab8488f6f47bf1fbe33010fd2d7e22b4db2e567783ce0b606db86b93759714c4f6396a7fb9f74c4021043b0f3d46d2633ebd43a877863df7d680f506587c119dd64100ca831ce2af33d951b524c5f06b49f5bf2cb381e74181930d06a80505c06abd5bf4870f0c9fb581bd80dba889660639f936edea8fe5d0c9eae58062ed693252583c71cc782ba613e01438e69b43f9e64eca84f9ea04e811ad7b39efd7876d1b6b501c4f48acce6f24239f6c04028788135cd88c3d15be0f2ebb7de9e9c19a7a93037005ee0a9a640bada332ec0d05ee9f08a832354a0487a927d5e88066e2569e6c5d4688e422bfa0b27c6171c6d7bf029bfd9165752af19aa71b33a1ea70b6c371fb21e47f527d80b7d04f582ad9f9935af723682dc01ca9880621870decb7ad15648cdf4ef153016f3e6d87933b8ec54cfa1fdf87c467020a3e753
print("Modulo N :", N)

e = 65537
print("Public Exponent e : ", e)

i = 0
nb_possibilite = 0

for p in resultat2:
	nb_possibilite += 1
	if (N % long(p.strip('\n'), 16) == 0):
		prime1 = p
		print("prime1 : ", prime1)
		i +=1
		p = long(p, 16)
		q = N / p
		print("prime2 : ", q)
		phi = (p-1)*(q-1)
		d = modinv(e, phi)
		print("Private Exponent d : ", d)

print("Nombre de possibilite : ", nb_possibilite)
print("Nombre de prime1 : ", i)
