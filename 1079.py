cases = int(input())

for i in range(cases):
    numbers = input()
    numbers = numbers.split()

    n1 = float(numbers[0])
    n2 = float(numbers[1])
    n3 = float(numbers[2])

    result = (n1*2 + n2*3 + n3*5)/10
    print('{:.1f}'.format(result))