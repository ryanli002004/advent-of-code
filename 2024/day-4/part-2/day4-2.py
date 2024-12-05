arr = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-4/part-1/input.txt", "r") as file:
    for line in file:
        arr.append(list(line.strip()))

visited = set()
height = len(arr) - 1
width = len(arr[0]) - 1
result = 0

# Directions for 8 possible moves (vertical, horizontal, and diagonal)
DIRECTIONS = [
    (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
    (-1, -1), (1, 1), (-1, 1), (1, -1)  # Diagonals: Up-Left, Down-Right, Up-Right, Down-Left
]

def check(r,c):
    global result
    goodset = set([("M","M","S","S"),("S","S","M","M"),("M","S","M","S"),("S","M","S","M")])
    if r > 0 and c > 0 and r<height and c<width and (arr[r-1][c-1],arr[r-1][c+1],arr[r+1][c-1],arr[r+1][c+1]) in goodset:
        result +=1

def dfs(r, c):
    visited.add((r, c))
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr <= height and 0 <= nc <= width and arr[nr][nc] == "A" and (nr, nc) not in visited:
            dfs(nr, nc)
    check(r, c)

for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == "A" and (r, c) not in visited:
            dfs(r, c)

print(result)