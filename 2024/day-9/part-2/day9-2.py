
filestring = None
with open("/Users/ryanli/Desktop/advent of code/2024/day-9/part-2/input.txt", "r") as file:
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


arroffiles = []
lefthashpointer = len(decodedstring)-1
righthashpointer = len(decodedstring)-1

while True:
    if lefthashpointer == -1:
        break
    while decodedstring[lefthashpointer] == ".":
        lefthashpointer-=1
    righthashpointer=lefthashpointer
    while lefthashpointer > 0 and decodedstring[lefthashpointer-1] == decodedstring[righthashpointer]:
        lefthashpointer-=1
    arroffiles.append((decodedstring[lefthashpointer],lefthashpointer,righthashpointer))
    lefthashpointer-=1
    righthashpointer = lefthashpointer


for file in range(len(arroffiles)):
    leftblankfinder = 0
    rightblankfinder = 0
    fileid = arroffiles[file][0]
    leftfileindex = arroffiles[file][1]
    rightfileindex = arroffiles[file][2]
    found = False

    while not found:
        rightblankfinder +=1
        while decodedstring[rightblankfinder] != ".":
            rightblankfinder +=1
        leftblankfinder = rightblankfinder
        if leftblankfinder > leftfileindex:
            break
        if rightfileindex-leftfileindex == 0:
            found = True
            break
        while decodedstring[rightblankfinder+1] == ".":
            rightblankfinder +=1
            if rightblankfinder-leftblankfinder == rightfileindex-leftfileindex:
                found = True
                break

    if found:
        for _ in range(rightblankfinder-leftblankfinder+1):
            temp = decodedstring[leftblankfinder]
            decodedstring[leftblankfinder] = decodedstring[leftfileindex]
            decodedstring[leftfileindex] = temp
            leftfileindex +=1
            leftblankfinder+=1


    
result = 0
for n in range(len(decodedstring)):
    if decodedstring[n] != ".":
        result +=  n*decodedstring[n]

print(result)

