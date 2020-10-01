cases = int(input())

for i in range(cases):
    n = input()
    count_leads = 0
    
    for x in range(len(n)):
        if(n[x] == '1'):
            count_leads += 2
        elif(n[x] == '2' or n[x] == '3' or n[x] == '5'):
            count_leads += 5
        elif(n[x] == '4'):
            count_leads += 4
        elif(n[x] == '6' or n[x] == '9' or n[x] == '0'):
            count_leads += 6
        elif(n[x] == '7'):
            count_leads += 3
        elif(n[x] == '8'):
            count_leads += 7
    
    print('{} leds'.format(count_leads))