plantmap = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-12/part-1/input.txt","r") as file:
    for line in file:
        plantmap.append(list(line.strip()))

totalcost = 0
visited = set()

width = len(plantmap[0])
height = len(plantmap)
perimeter = None
area = None
letter = None

def dfs(row,col):
    global perimeter,area,letter,height,width
    letter = plantmap[row][col]
    area +=1
    if row < height-1 and plantmap[row+1][col] == letter:
        if (row+1,col) not in visited:
            visited.add((row+1,col))
            dfs(row+1,col)
    else:
        perimeter+=1
    if row >0  and plantmap[row-1][col] == letter:
        if (row-1,col) not in visited:
            visited.add((row-1,col))
            dfs(row-1,col)
    else:
        perimeter+=1
    if col < width-1 and plantmap[row][col+1] == letter:
        if (row,col+1) not in visited:
            visited.add((row,col+1))
            dfs(row,col+1)
    else:
        perimeter+=1
    if col > 0 and plantmap[row][col-1] == letter:
        if (row,col-1) not in visited:
            visited.add((row,col-1))
            dfs(row,col-1)
    else:
        perimeter+=1

for row in range(len(plantmap)):
    for col in range(len(plantmap[0])):
        if (row,col) not in visited:
            perimeter = 0
            area = 0    
            visited.add((row,col))
            dfs(row,col)
            totalcost += perimeter * area

print(totalcost)