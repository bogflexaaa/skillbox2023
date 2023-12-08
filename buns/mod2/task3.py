s = input()
a = ""
b = ""
c = ""
for i in range(0,len(s)):
    if s[i] == " ":
        pars = i
        break
    a = a + s[i]
for i in range (pars+1,len(s)):
    if s[i] == " ":
        pars = i
        break
    b = b + s[i]
for i in range (pars+1,len(s)):
    c = c + s[i]
a = int(a)
b = int(b)
c = int(c)
if (a>=b and b>=c) or (c>=b and b>=a):
    if b!=a and b!=c:
        print (b)
if (b>=c and c>=a) or (a>=c and c>=b):
    if c!=a and c!=a:
        print (c)
if (b>=a and a>=c) or (c>=a and a>=b):
    if a!=b and a!=c:
        print (a)
if (a == c):
    print(a)
if (a == b):
    print(a)
if (b == c):
    print(b)