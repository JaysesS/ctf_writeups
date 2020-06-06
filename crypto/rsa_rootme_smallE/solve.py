from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Util.number import long_to_bytes, bytes_to_long
from sympy.ntheory.modular import crt
from sympy import root

f1 = open("clef0_pub.pem", "r")
f2 = open("clef1_pub.pem", "r")
f3 = open("clef2_pub.pem", "r")
key1 = RSA.importKey(f1.read())
key2 = RSA.importKey(f2.read())
key3 = RSA.importKey(f3.read())
message1 = open("m0", "r").read()
message2 = open("m1", "r").read()
message3 = open("m2", "r").read()

print("-"*20)
print("key 1:")
print(key1.n)
print(key1.e)
print("key 2:")
print(key2.n)
print(key2.e)
print("key 3:")
print(key3.n)
print(key3.e)
print("-"*20)

N = [key1.n,key2.n,key3.n]
C = [bytes_to_long(b64decode(message1)),bytes_to_long(b64decode(message2)),bytes_to_long(b64decode(message3))]
M = crt(N, C)[0]
m = root(M,3)
print("Result:")
print(long_to_bytes(m).decode())
print("-"*20)