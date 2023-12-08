a = input()
if not a.isdigit() or int(a) <= 0:
    print("Неверный ввод")
else:
    a = int(a)
    a2 = bin(a)[2:]
    a8 = oct(a)[2:]
    a16 = hex(a)[2:]
    print(a2+", "+a8+", "+a16)