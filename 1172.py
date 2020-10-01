x = []
for i in range(10):
    x.append(int(input()))

for i in range(len(x)):
    if(x[i] == 0 or x[i] < 0):
        x[i] = 1
        print('X[{}] = {}'.format(i, x[i]))
    else:
        print('X[{}] = {}'.format(i, x[i]))