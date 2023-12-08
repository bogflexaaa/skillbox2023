def solve(currentList):
    if len(set(currentList)) == 1:
        return "Все числа равны"
    elif len(set(currentList)) == len(currentList):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

newList = [0, 0, 0]
print(solve(newList))

newList = [1, 2, 3]
print(solve(newList))

newList = [1, 2, 3, 3]
print(solve(newList))

