result1 = []
result2 = []
result2hash = {}
similarity = 0
with open("/Users/ryanli/Desktop/advent of code/day-1/part-2/input.txt", "r") as file:
    for line in file:
        col1, col2 = line.split() 
        result1.append(int(col1))
        result2.append(int(col2))

for n in result2:
    result2hash[n] = 1 + result2hash.get(n,0)

for n in result1:
    if n in result2hash:
        similarity += n * result2hash[n]
print(similarity)