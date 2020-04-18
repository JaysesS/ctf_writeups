from base64 import b64decode
f = open('baby.onion', 'r').read().split('\n')[0]
res_hex = bytes.fromhex(str(f)).decode('utf-8')

while True:
    try:
        res_base = b64decode(res_hex).decode()
        res_hex = bytes.fromhex(str(res_base)).decode('utf-8')
    except:
        print(res_base)
        print(res_hex)
        break
