s = input()
k1 = 0
k2 = 0
flag = True
while 1:
    if len(s) != 0:
        a = s[0]
        s = s[1:]
        if flag:
            k1 += int(a)
            flag = False
        else:
            k2 += int(a)
            flag = True
    else:
        break
if (3 * k2 + k1) % 10 == 0:
    print('yes')
else:
    print('no')