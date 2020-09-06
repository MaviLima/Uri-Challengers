time = input().split(' ')

begin_hour = int(time[0])
end_hour = int(time[2])
begin_minute = int(time[1])
end_minute = int(time[3])

if(begin_hour == end_hour and begin_minute == end_minute):
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif(end_hour - begin_hour == 1):
    hour = 60
    if(begin_minute > end_minute):
        minute = 60 - (begin_minute - end_minute)
    else:
        minute = end_minute - begin_minute
    
    hour = hour - minute
    print('O JOGO DUROU 0 HORA(S) E {:.0f} MINUTO(S)'.format(minute))
else:
    hour = end_hour - begin_hour
    if(begin_minute > end_minute):
        minute = 60 - (begin_minute - end_minute)
    else:
        minute = end_minute - begin_minute

    print('O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)'.format(hour, minute))
