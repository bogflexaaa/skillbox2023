s = input()
k = 0
a = ""
i = s[len(s)-1]
for n in range(0,len(s)-2):
    a += s[n]
for n in range(0,len(a)):
    if a[n] == i:
        k +=1
    else:
        break
print(k)
