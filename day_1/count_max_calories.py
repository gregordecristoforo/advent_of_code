from itertools import groupby

calories_file = open('calories.txt', 'r')

elf_list = [list(group) for k, group in groupby(calories_file, lambda x: x == "\n") if not k]

total_calories_per_elf = []
for elf in elf_list:
    calories = [int(single_number.strip('\n')) for single_number in elf]
    total_calories_per_elf.append(sum(calories))

# part 1
print('part 1: ' + str(max(total_calories_per_elf)))

# part 2
total_calories_per_elf.sort()
print('part 2: ' + str(total_calories_per_elf[-1] + total_calories_per_elf[-2] + total_calories_per_elf[-3]))
