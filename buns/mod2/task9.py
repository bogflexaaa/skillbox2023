k1 = 0
k2 = 0
gl = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
s = input()
for i in range(0,len(s)):
    if s[i] in gl:
        k1+=1
    else:
        if s[i] != " ":
            k2+=1
print(k1,k2)
