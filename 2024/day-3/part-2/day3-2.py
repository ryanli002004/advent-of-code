import re

with open('/Users/ryanli/Desktop/advent of code/2024/day-3/part-2/input.txt', 'r') as file:
    content = file.read()

pattern = r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)"


# Find all matches in order
matches = re.finditer(pattern, content)

# Process matches to maintain exact order
results = []
for match in matches:
    full_match = match.group(0)  # Entire matched string
    # Check for do()
    if full_match == "do()":
        results.append("do")
    # Check for don't()
    elif full_match == "don't()":
        results.append("don't")
    # Check if it's mul(x, y)
    elif "mul" in full_match:
        results.append((match.group(1), match.group(2)))
add = True
result = 0
for n in results:
    if n == "do":
        add = True
    elif n == "don't":
        add = False
    else:
        if add == True:
            result += int(n[0])*int(n[1])
        
print(result)