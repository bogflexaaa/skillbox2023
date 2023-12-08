def solve(str):
    word = ""
    for i in str:
        if i in word:
            word = word.replace(i, "", 1)
        else:
            word = i + word
    if word == "":
        print("Палиндром создать нельзя")
    else:
        print(word)

str = input()
solve(str)