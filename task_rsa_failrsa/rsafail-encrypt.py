import Crypto.Util.number
import math

def generate_rsa_public_key():
    while True:
        e = 65537
        p = Crypto.Util.number.getPrime(256)
        q = Crypto.Util.number.getPrime(256)
        n = p * q
        phi = (p - 1) * (q - 1)
        if math.gcd(phi, e) == 1:
            return n, e


def encrypt_rsa(n, e, m):
    return list(map(str, [pow(ord(char), e, n) for char in m]))

def main():
    with open("flag.txt", "r") as f:
        FLAG = f.read()

    n, e = generate_rsa_public_key()
    encrypted = encrypt_rsa(n, e, FLAG)

    with open("encrypted.txt", "w") as f:
        f.write(f"""n = {n} e = {e} c = {" ".join(encrypted)}""")


if __name__ == "__main__":
    main()