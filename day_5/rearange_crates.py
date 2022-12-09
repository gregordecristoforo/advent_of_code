stack_1 = list('ZTFRWJG')
stack_2 = list('GWM')
stack_3 = list('JNHG')
stack_4 = list('JRCNW')
stack_5 = list('WFSBGQVM')
stack_6 = list('SRTDVWC')
stack_7 = list('HBNCDZGV')
stack_8 = list('SJNMGC')
stack_9 = list('GPNWCJDL')

ship = {'1': stack_1, '2': stack_2, '3': stack_3, '4': stack_4, '5': stack_5, '6': stack_6, '7': stack_7, '8': stack_8, '9': stack_9}

data = open('data.txt', 'r')

for line in data:
    if line[0] != 'm':
        continue
    print(line)
    line = line.replace('move ', '').replace('\n','')
    number_of_craits, rest = line.split(' from ')
    from_crait, rest = rest.split(' to ')
    to_crait = rest.replace(' to ','')
    for _ in range(int(number_of_craits)):
        crait = ship[from_crait].pop()  
        ship[to_crait].append(crait)

print(list(ship['1']))
print(list(ship['2']))
print(list(ship['3']))
print(list(ship['4']))
print(list(ship['5']))
print(list(ship['6']))
print(list(ship['7']))
print(list(ship['8']))
print(list(ship['9']))


###################### part 2 ##########################


stack_1 = list('ZTFRWJG')
stack_2 = list('GWM')
stack_3 = list('JNHG')
stack_4 = list('JRCNW')
stack_5 = list('WFSBGQVM')
stack_6 = list('SRTDVWC')
stack_7 = list('HBNCDZGV')
stack_8 = list('SJNMGC')
stack_9 = list('GPNWCJDL')

ship = {'1': stack_1, '2': stack_2, '3': stack_3, '4': stack_4, '5': stack_5, '6': stack_6, '7': stack_7, '8': stack_8, '9': stack_9}

data = open('data.txt', 'r')

for line in data:
    if line[0] != 'm':
        continue
    print(line)
    line = line.replace('move ', '').replace('\n','')
    number_of_craits, rest = line.split(' from ')
    from_crait, rest = rest.split(' to ')
    to_crait = rest.replace(' to ','')

    craits = ship[from_crait][-int(number_of_craits):]
    for i in craits:
        ship[to_crait].append(i)
        ship[from_crait].pop()

print(list(ship['1']))
print(list(ship['2']))
print(list(ship['3']))
print(list(ship['4']))
print(list(ship['5']))
print(list(ship['6']))
print(list(ship['7']))
print(list(ship['8']))
print(list(ship['9']))


