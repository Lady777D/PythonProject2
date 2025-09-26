n = int(input('введите количество дней'))

left = 'g'
central = 'c'
right = 'v'

for i in range(n):
    #действие Маши
    right, central = central, right
    #действие Тани
    left,  central = central, left

print(left + central + right)