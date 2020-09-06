count_pair = 0

for i in range(5):
    number = int(input())

    if(number%2 == 0):
        count_pair += 1

print('{} valores pares'.format(count_pair))