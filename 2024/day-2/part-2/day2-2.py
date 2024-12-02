
def isOk(linearr):
    strictdec = True
    strictinc = True
    for n in range(len(linearr)-1):
        if abs(linearr[n] - linearr[n+1]) > 3:
            return False
        if not (linearr[n] > linearr[n+1]):
            strictdec = False
        if not (linearr[n] < linearr[n+1]):
            strictinc = False
    return strictdec or strictinc
        
result = 0
with open("/Users/ryanli/Desktop/advent of code/2024/day-2/part-2/input.txt", "r") as file:
    for line in file:
        linearr = [int(num) for num in line.split()]
        if isOk(linearr):
            result+=1
            
        else:
            good = False
            for n in range(len(linearr)):
                if isOk(linearr[:n]+linearr[n+1:]):
                    good = True
            if good:
                result +=1
                
print(result)

