import prime
import rabin2

def read_in_chunks(file_object, chunk_size=17):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


p = 18810318778328561651
q = 22108713007868523767
n = p*q  # 415871939456586229616889854885818259317

print(f"Public key N = {n}")

check = 0
with open('notrsa.bmp.enc', 'rb') as f:
    with open("notrsa.bmp", "wb") as w:
        for peace in read_in_chunks(f):
            ciphertext = rabin2.decryption(int.from_bytes(peace, "big"), p, q)
            ciphertext_bytes = list(int.to_bytes(x, 17, 'big') for x in ciphertext)
            # print(list(hex(j) for j in ciphertext))
            # Try set header
            if check == 0:
                w.write(ciphertext_bytes[2][-16:])
            elif check == 1:
                w.write(ciphertext_bytes[3][-16:])
            elif check == 2:
                w.write(ciphertext_bytes[3][-16:])
            elif check == 3:
                w.write(ciphertext_bytes[1][-16:])
            check +=1
            for i in ciphertext_bytes:
                if i.count(b'\xff') > 3:
                    w.write(i[-16:])
            