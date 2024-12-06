rules = []
updates = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-5/part-1/input.txt", "r") as file:
    part = 1
    for line in file:
        if line.strip() == None:
            part = 2
        if line.strip() and part == 1:
            rules.append()