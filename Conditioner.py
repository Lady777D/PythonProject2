t_room = int(input('введите температуру в комнате'))
t_cond = int(input('введите желаемую температуру'))
mode = input('введите режим работы')

if mode=='auto':
    t = t_cond

if mode == 'fan':
    t = t_room

if mode == 'heat':
    if t_room < t_cond:
        t = t_cond
    else:
        t = t_room

if mode == 'freeze':
    if t_room > t_cond:
        t = t_cond
    else:
        t = t_room

print(t)