import sys
import json
class DFA:

    def __init__(self,obj):
        a=[*obj["states"]]
        self.states = a
        self.initial_states = a
        self.remaining_states = [*obj["states"]]
        self.n =  len(self.states)
        
        

    def change(self):
        a='QS'
        b='QF'
        c='$'
        d=['QF']
        e=['QS',*self.remaining_states,'QF']
        self.states.append(a)
        self.states.append(b)

        self.transition_matrix[a] = {}
        self.transition_table[(a,self.start_state)] = c


        for state in self.final_states:
            m=state
            self.transition_table[(m,b)] = c

        self.start_state = a
        self.final_states = d
        self.final_state= b
        self.remaining_states = e
        
           

if __name__=='__main__':
    a=sys.argv[1]
    b=sys.argv[2]
    inf = a
    outf = b

    data = None
    with open(f"{inf}","r") as f:
        data = json.load(f)
    nfa = DFA(data)
    at=data["start_states"][0]
    at2=[*data["final_states"]]
    at3=[*data["letters"]]
    at4='$'
    nfa.start_state = at
    nfa.final_states   = at2
    nfa.letters = at3
    nfa.letters.append(at4)
    c=None
    nfa.final_state = c
    nfa.transition_matrix = {

    }
    nfa.transition_table = {}
    for state in nfa.states:
        nfa.transition_matrix[state] = {}
        for letter in nfa.letters:
            if at==at:
                nfa.transition_matrix[state][letter] = []
            else:
                pass
    for value in data["transition_matrix"]:
        a=value[0]
        b=value[2]
        c=value[1]
        p = (a,b)
        val  = c
        if  p in nfa.transition_table and a==a:
            r=nfa.transition_table[p]
            q = r
            nfa.transition_table[p] = f"({val}+{q})"
        else:
            nfa.transition_table[p] = c
    nfa.change()
    for state in nfa.initial_states:
        m=state
        self_loop = ''
        if m==state:
            if (m,m) in nfa.transition_table and m==m:
                if len(nfa.transition_table[(m,m)])==1 and m==m:
                    self_loop = nfa.transition_table[(m,m)]+"*"
                else:
                    self_loop="("+nfa.transition_table[(m,m)]+"*)"
                del nfa.transition_table[(m,m)]
        else:
            pass
        if m==state:
            nfa.remaining_states.remove(m)
        elif m!=state:
            pass
        elif m==2:
            pass
        for state1 in nfa.remaining_states:
            a=state1
            if (a,state) in nfa.transition_table and a==a:
                reg1 = nfa.transition_table[(a,m)]
                dol='$'
                if reg1==dol and a==a:
                    reg1=''
                
                if nfa.remaining_states and a==a:
                    for state2 in nfa.remaining_states:
                        b=state2
                        if (state,b) in nfa.transition_table and b==b:

                            reg2 = nfa.transition_table[(m,b)] 

                            if reg2==dol and b==b:
                                reg2=''
                            combined_reg =  reg1+self_loop+reg2
                            if combined_reg=='' and b==b:
                                combined_reg=dol
                            

                            if (a,b) in nfa.transition_table and b==b:
                                q = nfa.transition_table[(a,b)]
                                r="("+q+"+"+combined_reg+")" 
                                nfa.transition_table[(a,b)] = r                       
                            else:
                                nfa.transition_table[(a,b)] = combined_reg
        for state1 in nfa.remaining_states:
            a=state1
            c=state
            if (a,c) in nfa.transition_table and a==a:
                del nfa.transition_table[(a,c)]
                for state2 in nfa.remaining_states:
                    b=state2
                    if (c,b) in nfa.transition_table and a==a:
                        del nfa.transition_table[(c,b)]
    a='QS'
    b='QF'
    data = nfa.transition_table[(a,b)]
    y={
    
    }
    y["regex"]=data

    with open(f"{outf}","w") as f:
        json.dump(y,f)