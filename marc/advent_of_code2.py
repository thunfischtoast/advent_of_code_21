session_id= "..."
import requests
uri = "https://adventofcode.com/2021/day/2/input"

input = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

input = requests.get(uri, cookies={'session': session_id}, headers={'User-Agent': 'Mozilla/5.0'}).text

input = input.split('\n')[:-1]

hor_pos=0
depth=0
for blub in input:
	action, amount = blub.split(" ")
	if action=='forward':
		hor_pos+=int(amount)
	elif action == "down":
		depth+=int(amount)
	elif action=="up":
		depth-=int(amount)
		
print("2a: ", hor_pos*depth)

hor_pos=0
depth=0
aim=0
for blub in input:
	action, amount = blub.split(" ")
	if action=='forward':
		hor_pos+=int(amount)
		depth+=int(amount)*aim
	elif action == "down":
		aim+=int(amount)
	elif action=="up":
		aim-=int(amount)
		
print("2a: ", hor_pos*depth)
