from base64 import b16decode, b32decode, b64decode
from pwn import *
from time import sleep
from re import sub
from string import ascii_uppercase

flgfmt = "DogeCTF{"
flgfmt2 = "DOGECTF{"

alphabets = list(ascii_uppercase + '{' + '}') 
numbers = [i for i in range(28)]
mapping_table = dict(zip(alphabets, numbers))
 
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None 
    else:
        return x % m

def affine_d(key1, key2, cts):
    cursor = list()
    plaintext = list()
    for c in cts:
        cursor.append((modinv(key1, 26) * (mapping_table[c] - key2)) % 26)
    for cur in cursor:
        for letter, num in mapping_table.items():
            if num == cur:
                plaintext.append(letter)
    plaintext[7] = '{'
    plaintext[-1] = '}'
    return ''.join(plaintext)

def atbash_d(cts):
    clear_text = ''
    for char in atbash_gen(cts):
        clear_text += char
    res = list(clear_text)
    res.insert(7, '{')
    res.append('}')
    return ''.join(res)

def atbash_gen(text):
    text = sub(r'\W', '', text)
    atbash = lambda c: chr(-ord(c) + 155)
    for char in text.upper():
        if char in '1234567890{}':
            yield char
        else:
            yield atbash(char)

def rail_d(cts, key=3): 
    rail = [['\n' for i in range(len(cts))]  
                for j in range(key)] 
        
    dir_down = None
    row, col = 0, 0
         
    for i in range(len(cts)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
            
        rail[row][col] = '*'
        col += 1
             
        if dir_down: 
            row += 1
        else: 
            row -= 1
                 
    index = 0
    for i in range(key): 
        for j in range(len(cts)): 
            if ((rail[i][j] == '*') and
            (index < len(cts))): 
                rail[i][j] = cts[index] 
                index += 1
            
    result = [] 
    row, col = 0, 0
    for i in range(len(cts)):   
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False    
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1      
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 

def rot(cts, key): 
    cipher_text = "" 
    for c in cts:
        if c.isalpha():
            if c.isupper():
                caps = True
            else:
                caps = False
            alphabet = ord(c.lower()) + key 
            if alphabet > ord('z'):
                alphabet -= 26
            letter = chr(alphabet)
            if caps is True:
                letter = letter.upper()
            cipher_text += letter
        else:
            cipher_text += c
    return cipher_text

def rots(cts):
    data =  [rot(cts, i) for i in range(30)]
    ans = [x for x in data if flgfmt in x]
    return ans[0]

def tts(cipa):
    cipa = cipa.replace('\n', '')
    print('get:', cipa)
    result = list()
    try:
        result.append(rots(cipa))
    except:
        pass
    try:    
        result.append(rail_d(cipa))
    except:
        pass
    try:
        result.append(atbash_d(cipa))
    except:
        pass
    try:
        result.append(affine_d(9, 6, cipa))
    except:
        pass
    try:
        result.append(b64decode(cipa).decode())
    except:
        pass
    try:
        result.append(b32decode(cipa).decode())
    except:
        pass
    try:
        result.append(b16decode(cipa).decode())
    except:
        pass

    ans = [x for x in result if flgfmt in x or flgfmt2 in x]
    return ans[0]

spl = '-----------------------------------------------------------------------'
c = remote("ctf.umbccd.io",5200)
sleep(1)
res = c.recv().decode().split(spl)[2]
c.sendline(tts(res))
i = 0
try:
    while True:
        res = c.recv().decode()
        ans = tts(res)
        print('>>', i)
        print("send:", ans)
        i+=1
        c.sendline(ans)
except:
    pass

# - rot13
# - rot16
# - base64
# - base32
# - base16
# - atbash
# - affine with b=6, a=9
# - railfence with key=3
