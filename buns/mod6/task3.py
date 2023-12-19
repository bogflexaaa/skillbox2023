def get_armstrong_numbers():
    for i in range(10, 100000):
        order = len(str(i))
        sum = 0
        current = i
        while current > 0:
            digit = current % 10
            sum += digit ** order
            current //= 10
        if i == sum:
            yield i

for i in range(8):
    print(next(get_armstrong_numbers()), end=' ')