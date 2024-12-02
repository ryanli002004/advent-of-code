
result = 0
with open("/Users/ryanli/Desktop/advent of code/2024/day-2/part-1/input.txt", "r") as file:
    for line in file:
        linearr = [int(num) for num in line.split()]
        print(linearr)
        IncorDec = None
        if linearr[1] > linearr[0]:
            IncorDec = "increasing"
        elif linearr[1] < linearr[0]:
            IncorDec = "decreasing"
        else:
            continue
        if IncorDec == "increasing":
            l = 1
            safe = True
            while l < len(linearr):
                if linearr[l] <= linearr[l-1]:
                    safe = False
                    break
                elif (linearr[l] - linearr[l-1]) > 3:
                    safe = False
                    break
                l +=1
            if safe:
                result +=1
        elif IncorDec == "decreasing":
            l = 1
            safe = True
            while l < len(linearr):
                if linearr[l] >= linearr[l-1]:
                    safe = False
                    break
                elif (linearr[l-1] - linearr[l]) > 3:
                    safe = False
                    break
                l +=1
            if safe:
                result +=1
    print(result)

