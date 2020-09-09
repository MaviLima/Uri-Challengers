number = int(input())

if(number != 0):
    for i in range(1, 10001):
        if(i%number == 2):
            print(i)