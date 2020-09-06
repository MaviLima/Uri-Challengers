salary = float(input())

impost = 0
if(salary >= 0 and salary <= 2000):
    print('Isento')
elif(salary >= 2000.01 and salary <= 3000):
    salary = salary - 2000
    if(salary <= 1000):
        impost += (salary*8)/100

    print('R$ {:.2f}'.format(impost))
elif(salary >= 3000.01 and salary <= 4500.00):
    salary = salary - 2000
    impost += (1000*8)/100
    impost += ((salary-1000)*18)/100
    print('R$ {:.2f}'.format(impost))
else:
    salary = salary - 2000
    impost += (1000*8)/100
    impost += (1500*18)/100
    impost += ((salary - 2500)*28)/100
    print('R$ {:.2f}'.format(impost))
