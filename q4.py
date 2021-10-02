import numpy as np
import sys
import json

with open(sys.argv[1]) as f:
    x = json.load(f)

a=x["start_states"][0]
# print(a)



result=list(map(lambda x:0,x["states"]))
# print(result)
arr=np.array(result)

# print(x["states"].index("Q0"))

arr[x["states"].index(a)]=1
# print(arr)
se=[]
se.append(a)

while len(se)>0:
    a=se.pop(0)
    arr[x["states"].index(a)]=1
    for alpha in x["letters"]:
        for arr2 in x["transition_matrix"]:
            if arr2[0]==a and arr2[1]==alpha:
                if arr[x["states"].index(arr2[2])]==0:
                    arr[x["states"].index(arr2[2])]=1
                    se.append(arr2[2])

part1=[]
part2=[]

for a in range(len(x["states"])):
    if arr[a]==1 and x["states"][a] in x["final_states"]:
        part1.append(a)
    elif arr[a]==1:
        part2.append(a)

# print(part1)
# print(part2)
fin=[]
fin.append(part1)
fin.append(part2)
# print(fin)
f=0
m=[]

ff=0
while f==0:
    compare=[]
    print(fin)
    for arr in fin:
        arr2=arr.copy()
        part1=[]
        part2=[]
        popped=arr2.pop(0)
        part1.append(popped)
        for item in arr2:
            statesarray=np.array(x["states"])
            state1=statesarray[popped]
            state2=statesarray[item]
            g=0

            #at this point item is other than 1st element and pooped is the first elemetn (indices)
            for item2 in x["letters"]:
                #item 2 is the letter
                state3=""
                state4=""
                for rws in x["transition_matrix"]:
                    if rws[0]==state1 and rws[1]==item2:
                        state3=rws[2]
                    if rws[0]==state2 and rws[1]==item2:
                        state4=rws[2]
                if item2=="b" and  popped==0 and item==5:
                    print("yolo")
                    print(state3)
                    print(state4)

                j=0
                k=0
                i=0
                for arr3 in fin:
                    if x["states"].index(state3) in arr3:
                        j=i
                    i+=1
                i=0
                for arr3 in fin:
                    if x["states"].index(state4) in arr3:
                        k=i
                    i+=1
                if j!=k:
                    g=1
            if g==1:
                print("fomo")
                part2.append(item)
            else:
                part1.append(item)
        compare.append(part1)
        if len(part2)!=0:
            compare.append(part2)
    print(compare)
    print(fin)
    print(2)

    h=0
    ff+=1
    if len(fin)!=len(compare):
        h=1
    else:
        arr=fin.copy()
        arr2=compare.copy()
        # print(len(fin))
        for i in range(len(fin)):
            a=arr.pop(0)
            b=arr2.pop(0)
            # print(a)
            # print(b)
            if set(a)!=set(b):
                h=1

    if h==0:
        break
    else:
        fin=compare.copy()
        # print(fin)
        # print("hmm")
    # print(compare)

# print(fin)
# print(ff)
y={
    
}

c=[]
for arr in fin:
    b=[]
    for a in arr:
        b.append(x["states"][a])

    c.append(b)


y["states"]=c

y["letters"]=x["letters"]
y["final_states"]=[]
for arr in y["states"]:
    for a in range(len(x["final_states"])):
        if x["final_states"][a] in arr:
            y["final_states"].append(arr)
            break

y["start_states"]=[]
for arr in y["states"]:
    for a in range(len(x["start_states"])):
        if x["start_states"][a] in arr:
            y["start_states"].append(arr)
            break


y["transition_matrix"]=[]
for arr in y["states"]:
    for str1 in x["letters"]:
        a=[]
        for str2 in arr:
            for k in range(len(x["transition_matrix"])):
                if x["transition_matrix"][k][0]==str2 and x["transition_matrix"][k][1]==str1:
                    for arr2 in y["states"]:
                        if x["transition_matrix"][k][2] in arr2:
                            a=arr2
                            break
                    break
            break



        ary=[]
        ary.append(arr)
        ary.append(str1)
        ary.append(list(a))
        y["transition_matrix"].append(ary)


with open(sys.argv[2], 'w') as json_file:
    json.dump(y, json_file)




























