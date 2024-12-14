robots = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-14/part-2/input.txt","r") as file:
    robots = [list(map(int,line.split()))for line in file]

width = 101 
height = 103 
heightmid = 51
widthmid = 50 

lowestsafteyfactor = float("inf")
bestiteration = float("inf")

for second in range(width*height):
    mapset = set()
    for robot in robots:
        mapset.add((robot[0],robot[1]))
        robot[0] = (robot[0]+robot[2])%width
        robot[1] = (robot[1]+robot[3])%height

    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0

    for robot in robots:
        if robot[0] < widthmid and robot[1] < heightmid:
            quad1+=1
        elif robot[0] > widthmid and robot[1] < heightmid:
            quad2+=1
        elif robot[0] < widthmid and robot[1] > heightmid:
            quad3+=1
        elif robot[0] > widthmid and robot[1] > heightmid:
            quad4+=1

    safteyfactor = quad1*quad2*quad3*quad4
    if len(mapset) == 500 and second<bestiteration:
        bestiteration = second

print(bestiteration)