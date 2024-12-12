with open("/Users/ryanli/Desktop/advent of code/2024/day-11/part-1/input.txt", 'r') as file:
    # Read the content of the file
    data = file.read().strip()

# Process the data into a list of integers
stones = list(map(int, data.split()))

for _ in range(25):
    stoneindex = 0
    while stoneindex<len(stones):
        if stones[stoneindex] == 0:
            stones[stoneindex] = 1
            stoneindex+=1
        elif len(str(stones[stoneindex])) % 2 == 0:
            lengthofstone = len(str(stones[stoneindex]))
            left_half = int(str(stones[stoneindex])[:lengthofstone // 2])
            right_half = int(str(stones[stoneindex])[lengthofstone // 2:])
            stones[stoneindex] = left_half
            stones.insert(stoneindex+1,right_half)
            stoneindex+=2
        else:
            stones[stoneindex] *= 2024
            stoneindex+=1
print(len(stones))