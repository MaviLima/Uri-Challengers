cases = int(input())

between = 0
out = 0

for i in range(cases):
    case = int(input())
    if(case >= 10 and case <= 20):
        between += 1
    else:
        out += 1

print('{} in'.format(between))
print('{} out'.format(out))