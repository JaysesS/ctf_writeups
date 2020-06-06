pwn 100	babypwn

Friend gave me a binary and idk what this magic means

nc pwn.bar 10000

Скачать binary

1. It's elf
2. IDA -> main func -> F5 (pseudocode)
3. See code: ida.c
4. "The gets () function reads characters from stdin and places them in the character array pointed to by str." - from documentation.
5. Buffer overflow v3 -> v6
6. See solve.py