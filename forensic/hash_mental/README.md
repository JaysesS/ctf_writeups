1.  Generate wordlist with gen.py

    python3 gen.py > wordlist.txt

2.  Run hashcat for md5 mode

    hashcat -m 0 -a 0 hash.txt wordlist.txt

3.  Done

    flag is: Azure-Botswana-Mango