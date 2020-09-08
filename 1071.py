x = int(input())
y = int(input())

first_number = min(x, y)
second_number = max(x, y)

sum_impar = 0

for i in range(first_number+1, second_number):
    if(i%2 != 0):
        sum_impar += i

print(sum_impar)