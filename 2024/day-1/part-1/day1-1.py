
result1 = []
result2 = []
difference = 0
with open("/Users/ryanli/Desktop/advent of code/2024/day-1/part-1/input.txt", "r") as file:
    for line in file:
        col1, col2 = line.split() 
        result1.append(int(col1))
        result2.append(int(col2))
result1.sort()
result2.sort()
for n in range(len(result1)):
    difference += abs(result1[n] - result2[n])


print(difference)