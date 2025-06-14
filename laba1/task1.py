numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
x = 0
y = 0
for z in range(len(numbers)):
    if(numbers[z] is None):
        x = z
    else:
        y+=numbers[z]
numbers[x] = (y/(len(numbers)))
print("список с none:", numbers)
#Программа рассчитана на один "None" в массиве типа integer любой длины
