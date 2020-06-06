from encrypted import *
import string

letters = list('abcdefghijklmnopqrstuvwxyz01234567890_{}')

def encrypt_all_symbols(n, e):
    res = list()
    for x in letters: 
        res.append(pow(ord(x), e, n))
    return res

def solve(enc_letters):
    for x in c:
        if x in enc_letters:
            print(letters[enc_letters.index(x)], end='')
    print()

enc_letters = encrypt_all_symbols(n, e)
solve(enc_letters)