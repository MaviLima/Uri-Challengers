salary = float(input())

def showPrint(salary, percent):
    new_salary = salary + ((salary*percent)/100)
    print('Novo salario: {:.2f}'.format(new_salary))
    print('Reajuste ganho: {:.2f}'.format(new_salary - salary))
    print('Em percentual: {} %'.format(percent))

if(salary >= 0 and salary <= 400):
    showPrint(salary, 15)
elif(salary >= 400.01 and salary <= 800):
    showPrint(salary, 12)
elif(salary >= 800.01 and salary <= 1200):
    showPrint(salary, 10)
elif(salary >= 1200.01 and salary <= 2000):
    showPrint(salary, 7)
elif(salary >= 2000):
    showPrint(salary, 4)