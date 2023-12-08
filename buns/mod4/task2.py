def solve(a, n):
    if n == 0:  # базовый случай: a^0 = 1
        return 1
    elif n % 2 == 0:  # если n четное
        return solve(a * a, n // 2)
    else:  # если n нечетное
        return a * solve(a, n - 1)

print(solve(2, 5))
print(solve(3, 3))