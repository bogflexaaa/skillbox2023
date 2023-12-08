s = input()
a = ""
for i in range(0,len(s)):
    if (s[i] == "+") or ((s[i]>='0') and (s[i]<='9')):
        a += s[i]
print(a)