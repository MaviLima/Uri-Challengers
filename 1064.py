count_positive = 0
positive = 0

for i in range(6):
    number = float(input())

    if(number > 0):
        count_positive += 1
        positive += number

print('{} valores positivos'.format(count_positive))
print('{:.1f}'.format(positive/count_positive))