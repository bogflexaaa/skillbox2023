s = input()
a = ""
b = ""
c = ""
for i in range(0,len(s)):
    if s[i] == ".":
        pars = i
        break
    a = a + s[i]
for i in range (pars+1,len(s)):
    if s[i] == ".":
        pars = i
        break
    b = b + s[i]
for i in range (pars+1,len(s)):
    c = c + s[i]
print(c)
print(b)
print(a)