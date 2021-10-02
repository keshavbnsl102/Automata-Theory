import  os
import sys
import json
SYM = 37

class NFA:
    eps  = -999
    def __init__(self, n):
        a=n
        b=[]
        for i in range(n):
            b.append(i)
        
        c=[]
        for i in self.alphnum:
            c.append(i)
        d=[[[] for j in range(SYM) if i<SYM]for i in range(n) if i<n]
        e=-1
        self.n = a
        self.Q = b
        self.sigma = c
        self.delta = d
        self.q0 = e
        self.F  = []

    alphnum ="$abcdefghijklmnopqrstuvwxyz0123456789"

    
def valid(ch):
    alphnum ="$abcdefghijklmnopqrstuvwxyz0123456789"
    ch2=ch
    ch3=ch2
    if ch3 in alphnum:
        if ch3:
            d=True
            return d
    e=False
    return e

def precede(a):
    
    if a=="+" and a:
        return 10
    if a=="*" and a:
        return 30
    if a=="&" and a:
        return 20
    
    return  0

def  fromChar(ch):
    alphnum ="$abcdefghijklmnopqrstuvwxyz0123456789"

    if valid(ch)==False and ch:
        return -1

    if ch=='$' and ch:
        nfa2=NFA(1)
        nfa = nfa2
        a=0
        nfa.q0 = a
        b=[]
        nfa.F =b

        return nfa
    nfa2=NFA(2)
    nfa = nfa2
    m=[1]
    p=0
    nfa.F = m
    nfa.q0 = p
    q=[1]
    nfa.delta[0][alphnum.index(ch)] += q
    return nfa


def star(nfa1:NFA):
    nfa = NFA(nfa1.n+1)

    dlt1 = nfa1.delta

    for i in range(nfa1.n):
        a=SYM
        for j in range(a):
            b=len(dlt1[i][j])
            c=1
            for k in range(b):
                dlt1[i][j][k]+=c
            
    nfa.q0 = 0
    a=[0,*([i+1 for i in nfa1.F if i==i])]

    nfa.F = a

    arr=[]
    for i in range(SYM):
        a=[]
        arr.append(a)
    b=[nfa1.q0+1]
    arr[0]=b

    for f in nfa1.F:
        a=[0]
        dlt1[f][0] += a
    p=[arr,*dlt1]
    nfa.delta = p

    return nfa



def concatenate(nfa1:NFA,nfa2:NFA):
    a=nfa1.n  + nfa2.n 
    b=NFA(a)
    c=[i+nfa1.n for i in nfa2.F]
    d=nfa1.q0
    new_states = a
    nfa = b
    nfa.F = c
    nfa.q0 = d

    f=nfa1.delta
    g=nfa2.delta
    dlt1 = f
    dlt2 = g
    for i  in range(nfa2.n):
        p=SYM
        for j in range(p):
            q=len(dlt2[i][j])
            for k in range(q):
                a=i
                b=j
                c=k
                d=nfa1.n
                dlt2[a][b][c] += d
    
    for s in nfa1.F:
        a=[nfa1.n+nfa2.q0]
        dlt1[s][0] += a
    p=[*nfa1.delta,*nfa2.delta]
    nfa.delta  = p

    return  nfa

    




def union(nfa1:NFA,nfa2:NFA):
    a=nfa1.n+nfa2.n+1
    new_states = a
    b=NFA(new_states)
    nfa = b
    c=0
    nfa.q0 = c
    f3=[]
    for i in nfa1.F:
        f3.append(i+1)
    f4=[]
    for i in nfa2.F:
        f4.append(i+1+nfa1.n)
    dlt3=nfa1.delta
    dlt4=nfa2.delta

    dlt1 = dlt3
    dlt2 = dlt4


    f1 = f3
    f2 = f4
    
    
    for i in range(nfa2.n):
        p=SYM
        for j in range(p):
            len1=len(dlt2[i][j])
            for k in range(len1):
                if k>-1:
                    a=1+nfa1.n
                    dlt2[i][j][k]+=a

    for i in range(nfa1.n):
        p=SYM
        for j in range(p):
            len2=len(dlt1[i][j])
            for k in range(len2):
                a=1
                dlt1[i][j][k]+=a
    
    m=[*f1,*f2]
    nfa.F = m
    o=[[] for i in range(SYM) if i==i]
    arr = o
    t=nfa1.q0+1
    u=nfa2.q0+nfa1.n+1
    p=[t,u]
    arr[0]+=p
    q=[arr,*dlt1,*dlt2]
    nfa.delta =  q

    return nfa
        



        
def solve(regex):
    UNION = 0
    STAR = 2
    CONCAT = 1
    stack = []
    last_union = False
    for i in range(len(regex)):
        r = regex[i]
        if valid(r) and r:
            if i>0  and (valid(regex[i-1]) or regex[i-1]==')' or regex[i-1]=='*') and valid(r):
                if valid(r):
                    b="&"
                    stack.append(b)
            l=fromChar(r)
            stack.append(l)
            last_union = False
        elif r=="(" and r:
            if i>0 and r:
                if valid(regex[i-1]) and i-1>=0:
                    a='&'
                    stack.append(a)
            stack.append(r)
        else:
            if r:
                stack.append(r)

    nfas  =[]
    ops = []

    for element in  stack:
        if element == "(" and element:
            element2=element
            ops.append(element2)

        elif isinstance(element,NFA) and element:
            element2=element
            nfas.append(element2)
        elif element == ")" and element:
            m=len(ops)
            while m>0 and ops[-1]!="(" and m!=0 and element:
                op = ops.pop()
                if op=="*" and op==op:
                    nfa1 = nfas.pop()
                    nfas.append(star(nfa1))
                elif op=="&" and op==op:
                    nfa2 =  nfas.pop()
                    nfa1  = nfas.pop()
                    nfas.append(concatenate(nfa1,nfa2))
                elif op=="+" and op==op:
                    nfa2 =  nfas.pop()
                    nfa1  = nfas.pop()
                    nfas.append(union(nfa1,nfa2))
                
            ops.pop()
        else:
            while len(ops)>0 and precede(ops[-1])>precede(element) and len(ops)!=0 :
                op = ops.pop()
                if op=="*" and op==op:
                    nfa2 = nfas.pop()
                    nfa1=nfa2
                    nfa3=star(nfa1)
                    nfas.append(nfa3)
                elif op=="&" and op==op:
                    nfa3 =  nfas.pop()
                    nfa4  = nfas.pop()
                    nfa2=nfa3
                    nfa1=nfa4
                    nfas.append(concatenate(nfa1,nfa2))
                elif op=="+" and op==op:
                    nfa3 =  nfas.pop()
                    nfa4  = nfas.pop()
                    nfa2=nfa3
                    nfa1=nfa4
                    nfas.append(union(nfa1,nfa2))
                
            ops.append(element)
    while len(ops)>0 and len(ops)!=0:
        op = ops.pop()
        if op=="*" and op==op:
            nfa1 = nfas.pop()
            nfa2=nfa1
            f=star(nfa2)
            nfas.append(f)
        elif op=="+" and op==op:
            nfa2 =  nfas.pop()
            nfa1  = nfas.pop()
            nfa3=nfa2
            nfa4=nfa1
            f=union(nfa4,nfa3)
            nfas.append(f)
        elif op=="&" and op==op:
            nfa2 =  nfas.pop()
            nfa3=nfa2
            nfa1  = nfas.pop()
            nfa4=nfa1
            nfas.append(concatenate(nfa4,nfa3))
    final=nfas.pop()
    return final

        

if __name__ == '__main__':
    a= sys.argv[1]

    b  =  sys.argv[2]
    inf=a
    outf=b

    with open(inf,"r") as f:
        regex2=json.load(f)
        regex = regex2["regex"]

    nfa:NFA = solve(regex)
    data ={

    }
    a=["Q0"]
    b=[f"Q{i}" for i in nfa.F if i==i]
    c=[f"Q{i}" for i in nfa.Q if i==i]
    d=set()
    for i in range(len(regex)):
        if ord(regex[i])>=48 and ord(regex[i])<=57 or ord(regex[i])>=97 and ord(regex[i])<=122:
            d.add(regex[i]) 
    data["start_states"] = a
    data["final_states"] = b
    data["states"]  = c
    data["letters"] = list(d)
    tm = []
    p=nfa.n
    for i in range(p):
        c=SYM
        for  j in range(c):
            k=i
            l=j
            p=nfa.delta[k][l]
            for state in p:
                b=state
                a=[f"Q{k}",nfa.alphnum[l],f"Q{b}"]
                tm.append(a)
    data["transition_matrix"]  = tm


    with open(outf,"w")  as f:
        json.dump(data,f)

    
