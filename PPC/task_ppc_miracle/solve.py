from pwn import *
from time import sleep
from datetime import datetime

def get_answer(res):
    time = [int(x) for x in res[4].split(':')]
    speed = float(res[2])
    d1 = datetime(2000, 1, 1, 0, 0, 0)
    d2 = datetime(2000, 1, 1, time[0], time[1], time[2])
    ans = int((d2 - d1).total_seconds()) / speed
    m = str(int((ans //60)%60))
    s = str(int(ans %60))
    if len(m) == 1:
        m = '0' + m
    if len(s) == 1:
        s = '0' + s
    return "{}:{}".format(m,s)

def test(a):
    a = a.split(' ')
    print(get_answer(a))

# test('I ran 4.8 in 0:44:00 What\'s my pace?')
con = remote('ctf.umbccd.io', 5300)
con.recv()
con.recv()
con.sendline('07:53\n')
print('Start...')

i = 0
while True:
    res = con.recv().decode()
    print(i, " > ", res)
    i+=1
    try:
        ans = get_answer(res.split(' '))
        con.sendline(ans)
    except:
        break

con.close()




