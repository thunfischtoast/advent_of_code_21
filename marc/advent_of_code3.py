session_id= "..."
import requests
uri = "https://adventofcode.com/2021/day/3/input"

input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

input = requests.get(uri, cookies={'session': session_id}, headers={'User-Agent': 'Mozilla/5.0'}).text

input_split = input.split('\n')[:-1]

summen=[]
for i in range(0,len(input_split[0])):
	summen.append(sum([int(j) for j in list("".join(input_split))[i::len(input_split[0])]]))
	
gamma = ['0b']
epsilon = ['0b']
devider = len(input_split)/2
for summe in summen:
	if (summe > devider):
		gamma.append("1")
		epsilon.append("0")
	else:
		gamma.append("0")
		epsilon.append("1")
		
gamma_str = "".join(gamma)
epsilon_str = "".join(epsilon)


print('3a:', int(gamma_str,2)* int(epsilon_str,2))

def bla_oxy(input_seq, index):
	index+=1
	if len(input_seq)==1:
		return input_seq[0]
	inputer = [int(j) for j in list("".join(input_seq)[index::len(input_seq[0])])]
	d = len(input_seq)/2
	if sum(inputer)>=d:
		return bla_oxy(list(filter(lambda x: x[index]=='1', input_seq)), index)
	else:
		return bla_oxy(list(filter(lambda x: x[index]=='0', input_seq)), index)


def bla_co2(input_seq, index):
	index+=1
	if len(input_seq)==1:
		return input_seq[0]
	inputer = [int(j) for j in list("".join(input_seq)[index::len(input_seq[0])])]
	d = len(input_seq)/2
	if sum(inputer)>=d:
		return bla_co2(list(filter(lambda x: x[index]=='0', input_seq)), index)
	else:
		return bla_co2(list(filter(lambda x: x[index]=='1', input_seq)), index)

print ("3b: ", int("0b"+bla_oxy(input_split,-1),2) * int("0b" + bla_co2(input_split,-1),2))
