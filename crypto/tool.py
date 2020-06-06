from random import randrange
from termcolor import colored
import gmpy2
import json

from Crypto.Util.number import long_to_bytes
from functools import reduce

arts = {
    0: """
             ._     __,
              |\,../'\\
            ,'. .     `.
           .--         '`.
          ( `' ,          ;
          ,`--' _,       ,'\\
         ,`.____            `.
        /              `,    |
       '                \,   '
       |                /   /`,
       `,  .           ,` ./  |
       ' `.  ,'        |;,'   ,@
 ______|     |      _________,_______
        `.   `.   ,'
         ,'_,','_,
         `'   `'
    """,
    1: """
                                               __
             ____               ________     ,',.`.
           \`''-.`-._..--...-'''        ```--':_ ) )
            `-.._` '              -..           ' /
     ,'`..__..'' -. _ `._                         \\
    ('';`      _ ,''       .-'            ,'       :
     `-._     `*/     ,                  '      .  |
        _.:._   `-'`-'  ;   \                  ,'  ;
     .':::::'`    ,' \,'     :         ;          /
      `-..__        ,'/      |       ,'         ,'
            ``---;'` \ `     ;.____..-'`.     ,'\\
                /   / \:    :            :   (\ `\\
              ,'  .'   \    :           ;'   / )  )
             /,_,.;::.  `.   \         /   ,',',_(:::.
                          `.  `.     ,'  ;'
                           /,_,'::. `-'`':
    """,
    2: """
     ,--.-'-,--.
     \  /-~-\  /
    / )' a a `( \\
   ( (  ,---.  ) )
    \ `(_o_o_)' /
     \   `-'   /
      | |---| |
      [_]   [_]
    """
}
banner = """
 _____ _____ _____    _____ _____ _____ __    
| __  |   __|  _  |  |_   _|     |     |  |   
|    -|__   |     |    | | |  |  |  |  |  |__ 
|__|__|_____|__|__|    |_| |_____|_____|_____|
"""
menu = """
[1] Classic RSA
[2] N E1 E2 C1 C2
[3] N1 N2 N3 E = 3 C1 C2 C3
[4] XOR A,B
[0] Exit
"""

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def ne1e2c1c2(n,e1,e2,c1,c2):

    def extended_euclidean(e1, e2):
        a = gmpy2.invert(e1, e2)
        b = (float(gcd(e1, e2)-(a*e1)))/float(e2)
        return a,b

    def modular_inverse(c1, c2, n):
        i = gmpy2.invert(c2, n)
        mx = pow(c1, a, n)
        my = pow(i, int(-b), n)
        m = mx * my % n
        return m

    a = 0 
    b = 0
    m = 0
    i = 0
    a,b = extended_euclidean(e1,e2)
    m = modular_inverse(c1, c2, n)
    return m

def classic_rsa(p,q,e,c, ctype):

    n = p * q
    en = (p-1) * (q-1)
    d = gmpy2.invert(e, en)
    if ctype == 1:
        c = int(c)
        return long_to_bytes(pow(c,d,n))
    else:
        c = c.split(',')
        return ''.join([chr(pow(int(ct),d,n)) for ct in c])

def n1n2n3e3c1c2c3(n1,n2,n3, c1, c2, c3, e = 3):
    from sympy.ntheory.modular import crt
    from sympy import root

    N = [n1,n2,n3]
    C = [c1,c2,c3]
    M = crt(N, C)[0]

    m = root(M,3)
    return m

def byte_xor(ba1, ba2):
    ba1 = ba1.encode()
    ba2 = ba2.encode()
    return bytearray(bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])).hex()

work = True
while work:
    print(colored(arts[randrange(3)], "white", attrs=['bold']))
    print("-" * 50)
    print(colored(banner, "blue", attrs=['bold']))
    print("-" * 50)
    print(colored(menu, "white", attrs=['bold']))
    try:
        c = int(input(">> "))
        if c == 0:
            work = False
        elif c == 1:
            print("Check values! Set Ctype 1. Big number 2. Array")
            input("Press Enter..")
            with open("values.json", "r") as read_file:
                values = json.load(read_file)
            try:
                print("Decoded:", classic_rsa(values['p'], values['q'], values['e'], values['c'], values['ctype']))
            except Exception as e:
                print(e)
                pass
            input("Press Enter..")
        elif c == 2:
            print("Check values!")
            input("Press Enter..")
            with open("values.json", "r") as read_file:
                values = json.load(read_file)
            try:
                print("Decoded:", ne1e2c1c2(values['n'], values['e1'], values['e2'], values['c1'], values['c2']))
            except Exception as e:
                print(e)
                pass
            input("Press Enter..")
        elif c == 3:
            print("Check values!")
            input("Press Enter..")
            with open("values.json", "r") as read_file:
                values = json.load(read_file)
            try:
                print("Decoded:", n1n2n3e3c1c2c3(values['n1'], values['n2'], values['n3'], values['c1'], values['c2'], values['c3']))
            except Exception as e:
                print(e)
                pass
            input("Press Enter..")
        elif c == 4:
            print("Input values for a ^ b")
            a = input("a: ")
            b = input("b: ")
            print("XORed:", byte_xor(a, b))
            input("Press Enter..")
    except ValueError as e:
        pass