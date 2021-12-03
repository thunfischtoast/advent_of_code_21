session_id= "..."
import requests
uri = "https://adventofcode.com/2021/day/1/input"
input = requests.get(uri, cookies={'session': session_id}, headers={'User-Agent': 'Mozilla/5.0'}).text

input_as_numbers = [int(i) for i in input.split('\n')[:-1]]
summed_triples = [sum(input_as_numbers[i:i+3]) for i in range(0,len(input_as_numbers)-2)]
count=0
count2=0

for i in range(0,len(input_as_numbers)-1):
    if input_as_numbers[i]<input_as_numbers[i+1]:
        count+=1
print("1a: " , count)

for i in range(0,len(summed_triples)-1):
    if summed_triples[i]<summed_triples[i+1]:
        count2+=1
print("1b: " , count2)
