s = input()
a = ""
b = ""
for i in range(0,len(s)):
    if s[i] == ",":
        zap = i
        break
    a = a + s[i]
for i in range(zap+2,len(s)):
    b = b + s[i]
print(int(a) % int(b))