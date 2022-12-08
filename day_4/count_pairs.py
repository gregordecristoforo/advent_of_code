data = open('data.txt', 'r')

overlapping_pairs = 0

for line in data:
    line = line.replace('\n','')
    first, second = line.split(',')
    first_lower, first_upper = first.split('-')
    second_lower, second_upper = second.split('-')
    if int(first_lower) <= int(second_lower) and int(first_upper) >= int(second_upper):
        overlapping_pairs += 1
        continue
    if int(second_lower) <= int(first_lower) and int(second_upper) >= int(first_upper):
        overlapping_pairs += 1
    
print('task 1: ' + str(overlapping_pairs))


data = open('data.txt', 'r')

overlapping_pairs = 0

for line in data:
    line = line.replace('\n','')
    first, second = line.split(',')
    first_lower, first_upper = first.split('-')
    second_lower, second_upper = second.split('-')
    if int(first_lower) > int(second_upper):
        continue
    if int(first_upper) < int(second_lower):
        continue
    overlapping_pairs += 1
print('task 2: ' + str(overlapping_pairs))
