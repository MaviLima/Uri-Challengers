cases = int(input())

for i in range(cases):
    case = int(input())
    
    if(case == 0):
        print('NULL')
    elif(case > 0):
        if(case%2 == 0):
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    else:
        if(case%2 == 0):
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')