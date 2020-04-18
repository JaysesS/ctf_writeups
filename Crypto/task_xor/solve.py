import os, sys

if len(sys.argv) != 3:
    print("usage: %s <filename> <outfile>" % sys.argv[0])
    sys.exit()

if os.path.exists(sys.argv[1]):
    key = 228 # replace 228 is key (use ord for str type)
    # like [chr(ord(a) ^ ord(b)) for a,b in zip(data, cycle(sys.argv[2]))]
    data = open(sys.argv[1]).read()
    xored = [chr(ord(a) ^ key) for a in data] 
    open(sys.argv[2], 'w').write(''.join(xored))
    print("Done")
 
else:
 print("%s: File not found" % sys.argv[1])