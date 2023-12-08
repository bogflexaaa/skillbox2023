s = input()
k0 = 0
k1 = 0
for i in range(0,len(s)):
    if s[i] == "0":
        k0 += 1
    else:
        k1 += 1
if k1 == k0:
    print('yes')
else:
    print('no')