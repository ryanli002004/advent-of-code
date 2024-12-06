import copy
arr = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-6/part-2/input.txt", "r") as file:
    for line in file:
        arr.append(list(line.strip()))
arr2 = copy.deepcopy(arr)
height = len(arr)
width = len(arr[0])

r = 0
c = 0



for x in range(height):
    for y in range(width):
        if arr[x][y] == "^":
            r = x
            c = y

r2 = r
c2 = c

direction = "up"

while r >= 0 and c >= 0 and r <= height-1 and c <= width-1:
    if arr[r][c] == ".":
        arr[r][c] = "^"
    if direction == "up":
        if arr[r-1][c] == "#":
            direction = "right"
        else:
            r-=1
    elif direction == "right":
        if arr[r][c+1] == "#":
            direction = "down"
        else:
            c+=1
    elif direction == "down":
        if arr[r+1][c] == "#":
            direction = "left"
        else:
            r+=1
    elif direction == "left":
        if arr[r][c-1] == "#":
            direction = "up"
        else:
            c-=1
    
result = 0
visited = set()

for x in range(height):
    for y in range(width):
        if arr[x][y] == "^":
            visited.add((x,y))

def checkloop(row,col):
    temparr = copy.deepcopy(arr2)
    temparr[row][col] = "#"
    tempc = c2
    tempr = r2
    loopcheckset = set()
    tempdirection = "up"
    while tempr >= 0 and tempc >= 0 and tempr <= height-1 and tempc <= width-1:
        if (tempr,tempc,tempdirection) in loopcheckset:
            return True
        loopcheckset.add((tempr,tempc,tempdirection))
        if tempdirection == "up":
            if tempr > 0 and temparr[tempr-1][tempc] == "#":
                tempdirection = "right"
            else:
                tempr-=1
        elif tempdirection == "right":
            if tempc < width-1 and temparr[tempr][tempc+1] == "#":
                tempdirection = "down"
            else:
                tempc+=1
        elif tempdirection == "down":
            if tempr< height-1 and temparr[tempr+1][tempc] == "#":
                tempdirection = "left"
            else:
                tempr+=1
        elif tempdirection == "left":
            if tempc > 0 and temparr[tempr][tempc-1] == "#":
                tempdirection = "up"
            else:
                tempc-=1
    return False

for row,col in visited:
    if checkloop(row,col):
        result+=1

print(result)