pair = 0
impar = 0
positive = 0
negative = 0

for i in range(5):
    number = float(input())

    if(number%2 == 0):
        pair += 1
    else:
        impar += 1
    
    if(number > 0):
        positive += 1
    elif(number < 0):
        negative += 1

print('{} valor(es) par(es)'.format(pair))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positive))
print('{} valor(es) negativo(s)'.format(negative))