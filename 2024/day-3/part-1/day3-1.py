with open('/Users/ryanli/Desktop/advent of code/2024/day-3/part-1/input.txt', 'r') as file:
    content = file.read()
character_array = list(content)
nums = ["0","1","2","3","4","5","6","7","8","9"]
l = 0
result = 0
while l < len(character_array):
    if character_array[l] == "m":
        l+=1
        if character_array[l] == "u":
            l+=1
            if character_array[l] == "l":
                l+=1
                if character_array[l] == "(":
                    l+=1
                    if character_array[l] in nums:
                        num1 = ""
                        while character_array[l] in nums:
                            num1 += character_array[l]
                            l+=1
                        if character_array[l] == ",":
                            l+=1
                            if character_array[l] in nums:
                                num2 = ""
                                while character_array[l] in nums:
                                    num2 += character_array[l]
                                    l+=1
                                if character_array[l] == ")":
                                    if len(num1) < 4 and len(num2) < 4:
                                        result += int(num1) * int(num2)
    l +=1

print(result)