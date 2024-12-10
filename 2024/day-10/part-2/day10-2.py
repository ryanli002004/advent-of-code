from collections import deque
topomap = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-10/part-1/input.txt", "r") as file:
    for line in file:
        topomap.append(list(line.strip()))

trailheads = []
result = 0

for r in range(len(topomap)):
    for c in range(len(topomap[0])):
        if topomap[r][c] == "0":
            trailheads.append([r,c])

def bfs(r,c):
    global result
    height = len(topomap)
    width = len(topomap[0])
    q = deque()
    q.append([r,c,0])
    while q:
        row,col,num = q.popleft()
        if num == 9:
            result +=1
        else:
            if row<height-1 and int(topomap[row+1][col]) == num+1:
                q.append([row+1,col,num+1])
            if col<width-1 and int(topomap[row][col+1]) == num+1:
                q.append([row,col+1,num+1])
            if row>0 and int(topomap[row-1][col]) == num+1:
                q.append([row-1,col,num+1])
            if col>0 and int(topomap[row][col-1]) == num+1:
                q.append([row,col-1,num+1])


for row,col in trailheads:
    bfs(row,col)

print(result)