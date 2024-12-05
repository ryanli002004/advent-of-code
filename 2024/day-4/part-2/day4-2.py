arr = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-4/part-2/input.txt", "r") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        arr.append(row)

