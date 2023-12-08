s = input()
a = ""
for i in range(0,len(s)):
    if s[i] == " ":
        a += s[i-1]
a += s[len(s)-1]
print(a)