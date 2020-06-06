import prime
import rabin2


def read_in_chunks(file_object, chunk_size=16):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


if __name__ == '__main__':
    p = prime.generate_a_prime_number(64)
    q = prime.generate_a_prime_number(64)
    n = p*q  # 415871939456586229616889854885818259317
    print(f"Public key N = {n}")

    with open('image.bmp', 'rb') as f:
        with open("image.bmp.enc", "wb") as w:
            for piece in read_in_chunks(f):
                ciphertext = rabin2.encryption(int.from_bytes(piece, "big"), n)
                w.write(int.to_bytes(ciphertext, 17, "big"))
