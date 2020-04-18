import os

def f_part():

    f = open('task.png', 'rb').read()
    f = f.split(b'\x89\x50\x4e\x47')
    c = 0
    for i in f:
        ib = bytes(i)
        open('res/' + str(c) + '.png', 'wb').write(b'\x89\x50\x4e\x47' + ib)
        c += 1

def s_part():

    from PIL import Image

    dira = '/home/jayse/writeups/task_ppc_split_and_create_image/res/'
    img = Image.new('RGB', (450, 300))
    i = 1
    try:
        for j in range(0, 450):
            for h in range(0, 300):
                imaga = Image.open(dira + str(i) + '.png')
                img.paste(imaga, (j,h))
                i +=1
    except Exception:
        pass
    img.save("out.jpg")

# f_part()
s_part()