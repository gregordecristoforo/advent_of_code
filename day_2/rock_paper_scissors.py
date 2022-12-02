data = open('data.txt', 'r')

points_per_line = {}
points_per_line['A X'] = 4        
points_per_line['A Y'] = 8
points_per_line['A Z'] = 3
points_per_line['B X'] = 1
points_per_line['B Y'] = 5
points_per_line['B Z'] = 9
points_per_line['C X'] = 7
points_per_line['C Y'] = 2
points_per_line['C Z'] = 6

score = 0
for line in data:
    score += points_per_line[line.replace("\n","")]

print('part 1: ', score)
    
data = open('data.txt', 'r')

points_per_line = {}
points_per_line['A X'] = 3
points_per_line['A Y'] = 4
points_per_line['A Z'] = 8
points_per_line['B X'] = 1
points_per_line['B Y'] = 5
points_per_line['B Z'] = 9
points_per_line['C X'] = 2
points_per_line['C Y'] = 6
points_per_line['C Z'] = 7

score = 0
for line in data:
    score += points_per_line[line.replace("\n","")]

print('part 2: ', score)
