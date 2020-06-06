from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Util.number import long_to_bytes, bytes_to_long
import gmpy2

class RSAModuli:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.m = 0
        self.i = 0
    def gcd(self, num1, num2):
        
        if num1 < num2:
            num1, num2 = num2, num1
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1
    def extended_euclidean(self, e1, e2):
        self.a = gmpy2.invert(e1, e2)
        self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)

    def modular_inverse(self, c1, c2, N):
        i = gmpy2.invert(c2, N)
        mx = pow(c1, self.a, N)
        my = pow(i, int(-self.b), N)
        self.m= mx * my % N
    def print_value(self):
        # print("Plain Text: ", self.m)
        return self.m

f1 = open("key1_pub.pem", "r")
f2 = open("key2_pub.pem", "r")
key1 = RSA.importKey(f1.read())
key2 = RSA.importKey(f2.read())
message1 = open("message1", "r").read()
message2 = open("message2", "r").read()

c = RSAModuli()
N  = key1.n
c1 = bytes_to_long(b64decode(message1))
c2 = bytes_to_long(b64decode(message2))
e1 = key1.e
e2 = key2.e
print(N)
print(c1)
print(c2)
print(e1)
print(e2)
c.extended_euclidean(e1, e2)
c.modular_inverse(c1, c2, N)
p = long_to_bytes(c.print_value())
print(p)
