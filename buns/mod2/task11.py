s = input()
newS = ""
flag = bool(0)
for i in range(0,len(s)):
    if s[i] != " ":
        newS+=s[i]
for i in range(0,len(newS)):
    for j in range(i+1,len(newS)-1):
        if newS[i] == newS[j]:
            flag = 1
            break
if flag == 1:
    print(True)
else:
    print(False)

        