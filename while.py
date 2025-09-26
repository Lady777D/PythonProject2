nam1 =0
nam2 =0
namber = 123456
print(nam1, nam2)
while namber != 0:
    namber = int(input('введите число'))
    if namber > 0:
        nam1 += 1
    if namber < 0:
        nam2 +=  1
print(nam1, nam2)