with open("/Users/ryanli/Desktop/advent of code/2024/day-11/part-2/input.txt", 'r') as file:
    # Read the content of the file
    data = file.read().strip()

# Process the data into a list of integers
stonecountmap = {}
stones = list(map(int, data.split()))
for i in stones:
    if i not in stonecountmap:
        stonecountmap[i] = 1
    else:
        stonecountmap[i] +=1
#for 25 it should be 194557
for _ in range(75):
    newstonecountmap = {}
    for key in stonecountmap.keys():
        if key == 0:
            if 1 in newstonecountmap:
                newstonecountmap[1] += stonecountmap[key]
            else:
                newstonecountmap[1] = stonecountmap[key]
        elif len(str(key)) % 2 == 0:
            lengthofstone = len(str(key))
            left_half = int(str(key)[:lengthofstone // 2])
            right_half = int(str(key)[lengthofstone // 2:])
            if left_half in newstonecountmap:
                newstonecountmap[left_half] += stonecountmap[key]
            else:
                newstonecountmap[left_half] = stonecountmap[key]           
            if right_half in newstonecountmap:
                newstonecountmap[right_half] += stonecountmap[key]
            else:
                newstonecountmap[right_half] = stonecountmap[key]
        else:
            if key*2024 in newstonecountmap:
                newstonecountmap[key*2024] += stonecountmap[key]
            else:
                newstonecountmap[key*2024] = stonecountmap[key]

    stonecountmap = newstonecountmap

result = 0
for value in stonecountmap.values():
    result += value

print(result)