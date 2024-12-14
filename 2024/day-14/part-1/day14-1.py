robots = []
with open("/Users/ryanli/Desktop/advent of code/2024/day-14/part-1/input.txt","r") as file:
    robots = [list(map(int,line.split()))for line in file]
#x=0 y=4 x+=3 y+=-3

width = 101 #101
height = 103 #103
for _ in range(100):

    for robot in robots:
        robot[0] = (robot[0]+robot[2])%width
        robot[1] = (robot[1]+robot[3])%height

quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0
heightmid = 51 #52
widthmid = 50 #51

for robot in robots:
    if robot[0] < widthmid and robot[1] < heightmid:
        quad1+=1
    elif robot[0] > widthmid and robot[1] < heightmid:
        quad2+=1
    elif robot[0] < widthmid and robot[1] > heightmid:
        quad3+=1
    elif robot[0] > widthmid and robot[1] > heightmid:
        quad4+=1

print(quad1*quad2*quad3*quad4)