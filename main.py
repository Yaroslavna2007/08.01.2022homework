# шифратор/дишифратор с ключом - словом

print('Что вы хотите: зашифровать или расшифровать')
w = input()
if w != 'зашифровать' and w!='расшифровать':
    print('Введите нужное слово.')
if w == 'зашифровать':
    x = str(input('Введите строчку.'))
    a = ' abcdefghijklmnopqrstuvwxyz'
    key = input('введите ключ ')
    for y in range(len(x)):
        s = a.find(x[y])
        t = a.find(key[y])
        d = s + t
        if d > 25:
            d = d - 25
            print(a[d],end = '')
        else:
            print(a[d],end = '')
if w == 'расшифровать':
    x = str(input('введите строчку '))
    a = 'abcdefghijklmnopqrstuvwxyz'
    key = input('введите ключ ')
    for y in range(len(x)):
        s = a.find(x[y])
        t = a.find(key[y])
        d = s - t - 1
        if d<0:
            d = s - t - 2
            print(a[d], end='')
        elif d > 25:
            d = d - 25
            print(a[d], end='')
        else:
            print(a[d], end='')