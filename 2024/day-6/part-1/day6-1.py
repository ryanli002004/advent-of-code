arr = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-6/part-1/input.txt", "r") as file:
    for line in file:
        arr.append(list(line.strip()))

height = len(arr)
width = len(arr[0])

r = 0
c = 0

for x in range(height):
    for y in range(width):
        if arr[x][y] == "^":
            r = x
            c = y

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

for x in range(height):
    for y in range(width):
        if arr[x][y] == "^":
            result+=1

print(result)