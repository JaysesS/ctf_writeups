from pwn import *
from base64 import b64encode, b64decode

con = remote('crypto.ctf.umbccd.io', 13371)
con.sendline('flg')
flg = con.recv()
con.close()
con = remote('crypto.ctf.umbccd.io', 13371)
con.send(b'enc:' + flg)
print(con.recv().decode())
