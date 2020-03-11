import string
file = open('empty.txt', 'rb').read()
hexed = ' '.join([hex(x)[2:] for x in list(file)])
open('hexed.txt', 'w').write(hexed)
# http://www.endmemo.com/unicode/unicodeconverter.php
# insert hexed to UTF-8 field and get Escaped Unicode
# in converted_to_unicode.txt
in_unicode = open('converted_to_unicode.txt').read()
in_unicode = [x for x in in_unicode.split('\\u')]
unique = set(in_unicode)
unique = sorted(list(unique))[1:]
# unique.remove('A0')
hexed_alfa = list((string.hexdigits).replace('ABCDEF', ''))
print(unique, len(unique), len(hexed_alfa))
print(hexed_alfa)
res = ''
for i in in_unicode:
    try:
        print(i, hexed_alfa[unique.index(i)])
        res += hexed_alfa[unique.index(i)]
    except ValueError:
        pass

print(res)