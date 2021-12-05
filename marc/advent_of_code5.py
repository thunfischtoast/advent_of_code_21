session_id= "..."
import requests
uri = "https://adventofcode.com/2021/day/5/input"



class Line:

    def __init__(self, ax, ay, bx, by):
        self.pointAx = int(ax)
        self.pointBx = int(bx)
        self.pointAy = int(ay)
        self.pointBy = int(by)


    @property
    def isHorizontal(self):
        return self.pointAy == self.pointBy

    @property
    def isVertical(self):
        return self.pointAx == self.pointBx

    @property
    def isMoep(self):
        return self.isHorizontal or self.isVertical

    def vector(self):
        x = my_range(self.pointAx, self.pointBx)
        y = my_range(self.pointAy, self.pointBy)
        return zip(x,y)

    def __repr__(self):
        return "%s,%s -> %s,%s" % (self.pointAx, self.pointAy, self.pointBx, self.pointBy)

def my_range(a,b):
    if a<b:
        return range(a,b+1)
    else:
        return range(a,b-1,-1)

input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

input = requests.get(uri, cookies={'session': session_id}, headers={'User-Agent': 'Mozilla/5.0'}).text

input = input.split('\n')[:-1]

lines = []

for line in input:
    lines.append(Line(*line.replace(" -> ", ",").split(",")))

grid = {}

for line in filter(lambda x: x.isHorizontal, lines):
    grid.setdefault(line.pointAy, [set(), set()])
    for a in my_range(line.pointAx, line.pointBx):
        if a in grid[line.pointAy][0]:
            grid[line.pointAy][1].add(a)
        else:
            grid[line.pointAy][0].add(a)

for line in filter(lambda x: x.isVertical, lines):
    for a in my_range(line.pointAy, line.pointBy):
        grid.setdefault(a, [set(), set()])
        if line.pointAx in grid[a][0]:
            grid[a][1].add(line.pointAx)
        else:
            grid[a][0].add(line.pointAx)


print ("5a:", sum([len(a[1]) for a in grid.values()]))


for line in filter(lambda x: not x.isMoep, lines):
    for l in line.vector():
        grid.setdefault(l[1], [set(), set()])
        if l[0] in grid[l[1]][0]:
            grid[l[1]][1].add(l[0])
        else:
            grid[l[1]][0].add(l[0])


print ("5b:", sum([len(a[1]) for a in grid.values()]))
