import numpy as np
import random
import json
import sys


with open(sys.argv[1]) as f:
	x = json.load(f)

print(x)
y={
	
}

y["letters"]=x["letters"]
y["states"]=[]
start_states=[]
start_states.append(x["start_states"])
y["start_states"]=start_states
# print(y["start_states"])
y["transition_matrix"]=[]
y["final_states"]=[]
for a in range(pow(2,len(x["states"]))):
	i=0
	z=[]
	m=a
	while m>0:
		n=m%2
		if n==1:
			z.append(x["states"][i])
		m=int(m/2)
		i+=1
	y["states"].append(z)

for arr in y["states"]:
	for str1 in x["letters"]:
		a=set()
		for str2 in arr:
			for k in range(len(x["transition_matrix"])):
				if x["transition_matrix"][k][0]==str2 and x["transition_matrix"][k][1]==str1:
					a.add(x["transition_matrix"][k][2])

		ary=[]
		ary.append(arr)
		ary.append(str1)
		ary.append(list(a))
		y["transition_matrix"].append(ary)
# print(y["transition_matrix"])


for arr in y["states"]:
	for a in range(len(x["final_states"])):
		if x["final_states"][a] in arr:
			y["final_states"].append(arr)
			break
# print(y["final_states"])


with open(sys.argv[2], 'w') as json_file:
	json.dump(y, json_file)




