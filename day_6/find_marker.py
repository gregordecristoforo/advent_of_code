data = open('data.txt','r')

for line in data:
    line = line.replace('\n','')
    for i in range(3,len(line)):
        buffer = line[i-3:i+1]
        buffer_without_duplicates = result = "".join(dict.fromkeys(buffer))
        if buffer == buffer_without_duplicates:
            print('marker is at position:' + str(i+1))
            break


################### part 2 #################


data = open('data.txt','r')

for line in data:
    line = line.replace('\n','')
    for i in range(13,len(line)):
        buffer = line[i-13:i+1]
        buffer_without_duplicates = result = "".join(dict.fromkeys(buffer))
        if buffer == buffer_without_duplicates:
            print('marker is at position:' + str(i+1))
            break

