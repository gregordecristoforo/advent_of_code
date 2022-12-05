data = open('data.txt','r')

common_character = []
for line in data:
    line = line.replace('\n','')
    length = len(line)
    first_pocket = line[:int(length/2)]
    second_pocket = line[int(length/2):]
    common_character.append(''.join(set(first_pocket).intersection(second_pocket)))

priority_sum = 0
for i in common_character:
    ascii_value = ord(i)
    if ascii_value> 64 and ascii_value< 91:
        priority = ascii_value - 38
    
    if ascii_value> 96 and ascii_value< 123:
        priority = ascii_value - 96
    priority_sum += priority 

print('part 1: ' + str(priority_sum))



three_elvs = ''
common_types = []
data = open('data.txt','r')
for i, lines in enumerate(data):
    index = i % 3
    lines = lines.replace('\n','')
    if index == 0:
        three_elvs = lines
    if index == 1:
        common_character = ''.join(set(three_elvs).intersection(lines))
    if index == 2:
        common_character = ''.join(set(common_character).intersection(lines))
        common_types.append(common_character)
        common_character = ''

priority_sum = 0
for i in common_types:
    ascii_value = ord(i)
    if ascii_value> 64 and ascii_value< 91:
        priority = ascii_value - 38
    
    if ascii_value> 96 and ascii_value< 123:
        priority = ascii_value - 96
    priority_sum += priority 

print('part 2: ' + str(priority_sum))

