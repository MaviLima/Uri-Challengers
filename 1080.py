position = 0
bigger = 0

for i in range(1, 101):
    n = int(input())

    if(n > bigger):
        bigger = n
        position = i

print(bigger)
print(position)