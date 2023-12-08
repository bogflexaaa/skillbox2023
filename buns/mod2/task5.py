s = input()
a = int(97)
b = int(122)
i = s[0]
temp = 2
n = s[2]
while temp != len(s)-1:
    temp += 1
    n += s[temp]
n = int(n)
k = ord(i)+n
if (k > b):
    k = a+(k-b-1)
if (k < a):
    k = b+(k-a-1)
print(chr(k))