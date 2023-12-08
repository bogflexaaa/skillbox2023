def algEvklid(a, b):
    if b == 0:
        return a
    else:
        return algEvklid(b, a % b)

print(algEvklid(32, 48))
print(algEvklid(24, 32))