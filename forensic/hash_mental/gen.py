colors = [x for x in open('colors.txt', 'r').read().split('\n')]
countries = [x for x in open('countries.txt', 'r').read().split('\n')]
fruit = [x for x in open('fruits.txt', 'r').read().split('\n')]
for i in colors:
    for j in countries:
        for z in fruit:
            print('{}-{}-{}'.format(i.capitalize().replace(" ", ""),j.capitalize().replace(" ", ""),z.capitalize().replace(" ", "")))
