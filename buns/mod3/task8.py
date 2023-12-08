#print('+' + "".join(c for c in input() if  c.isdecimal()))
print('+' + ''.join(filter(str.isdigit, input())))