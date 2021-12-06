####################################
# Setup
session_id= "..."
import requests
import collections
uri = "https://adventofcode.com/2021/day/6/input"

input = """3,4,3,1,2
"""

input = requests.get(uri, cookies={'session': session_id}, headers={'User-Agent': 'Mozilla/5.0'}).text

input = input.split('\n')[:-1]       

bla = {}
for fish in input[0].split(","):
    bla.setdefault(int(fish), 0)
    bla[int(fish)]+=1

bla = dict(sorted(bla.items()))
####################################
# Helper
def blub(bla, days):
    while days >0:
        bla2 = {}
        items = list(bla.items())
        timer = items[0][0] + 1
        for item in items[1:]:
            bla2[item[0]-timer] = item[1]
            
        bla2.setdefault(6, 0)
        bla2[6] += items[0][1]
        bla2[8] = items[0][1]
        bla = dict(sorted(bla2.items()))
        days -= timer
    return sum(bla.values())
####################################
# Stuff

print("6a:", blub(bla, 80))
print("6b:", blub(bla, 256))
