
filestring = None
with open("/Users/ryanli/Desktop/advent of code/2024/day-9/part-1/input.txt", "r") as file:
    for line in file:
        filestring = list(line.strip())
    
decodedstring = []
count = 0
blank = False
for num in filestring:
    if blank:
        for x in range(int(num)):
            decodedstring.append(".")
        blank = False
    else:
        for x in range(int(num)):
            decodedstring.append(count)
        count+=1
        blank = True

l = 0
r = len(decodedstring)-1

while decodedstring[l] != ".":
    l+=1

while l < r:
    while l<r and decodedstring[l] != ".":
        l+=1
    while l<r and decodedstring[r] == ".":
        r-=1
    temp = decodedstring[l]
    decodedstring[l] = decodedstring[r]
    decodedstring[r] = temp
    l+=1
    r-=1

result = 0
for n in range(len(decodedstring)):
    if decodedstring[n] != ".":
        result +=  n*decodedstring[n]

print(result)

