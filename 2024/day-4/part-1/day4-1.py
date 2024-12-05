arr = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-4/part-1/input.txt", "r") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        arr.append(row)
print(arr)
visited = set()
height = len(arr)-1
width = len(arr[0])-1
result = 0

def dfs(r,c):
    global result
    visited.add((r,c))
    if r > 0 and arr[r-1][c] == "X" and (r-1,c) not in visited:
        dfs(r-1,c)
    if r < height and arr[r+1][c] == "X" and (r+1,c) not in visited:
        dfs(r+1,c)
    if c > 0 and arr[r][c-1] == "X" and (r,c-1) not in visited:
        dfs(r,c-1)
    if c < width and arr[r][c+1] == "X" and (r,c+1) not in visited:
        dfs(r,c+1)
    if r > 0 and c > 0 and arr[r-1][c-1] == "X" and (r-1,c-1) not in visited:
        dfs(r-1,c-1)
    if c < width and r < height and arr[r+1][c+1] == "X" and (r+1,c+1) not in visited:
        dfs(r+1,c+1)
    if r > 0 and c < width and arr[r-1][c+1] == "X" and (r-1,c+1) not in visited:
        dfs(r-1,c+1)
    if r < height and c > 0 and arr[r+1][c-1] == "X" and (r+1,c-1) not in visited:
        dfs(r+1,c-1)
    if r > 0 and arr[r-1][c] == "M":
        if r > 1 and arr[r-2][c] == "A":
            if r > 2 and arr[r-3][c] == "S":
                result+=1
    if r < height and arr[r+1][c] == "M":
        if r < height-1 and arr[r+2][c] == "A":
            if r < height-2 and arr[r+3][c] == "S":
                result+=1
    if c > 0 and arr[r][c-1] == "M":
        if c > 1 and arr[r][c-2] == "A":
            if c > 2 and arr[r][c-3] == "S":
                result+=1
    if c < width and arr[r][c+1] == "M":
        if c < width-1 and arr[r][c+2] == "A":
            if c < width-2 and arr[r][c+3] == "S":
                result+=1
    if r > 0 and c > 0 and arr[r-1][c-1] == "M":
        if r > 1 and c > 1 and arr[r-2][c-2] == "A":
            if r > 2 and c > 2 and arr[r-3][c-3] == "S":
                result+=1
    if r > 0 and c < width and arr[r-1][c+1] == "M":
        if r > 1 and c < width-1 and arr[r-2][c+2] == "A":
            if r > 2 and c < width-2 and arr[r-3][c+3] == "S":
                result+=1
    if r < height and c < width and arr[r+1][c+1] == "M":
        if r < height-1 and c < width-1 and arr[r+2][c+2] == "A":
            if r < height-2 and c < width-2 and arr[r+3][c+3] == "S":
                result+=1
    if c > 0 and r < height and arr[r+1][c-1] == "M":
        if c > 1 and r < height-1 and arr[r+2][c-2] == "A":
            if c > 2 and r < height-2 and arr[r+3][c-3] == "S":
                result+=1

for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == "X" and (r,c) not in visited:
            dfs(r,c)
print(result)