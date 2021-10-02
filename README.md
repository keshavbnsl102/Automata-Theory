## Automata assignment
## Name: Keshav Bansal
## Roll number: 2019101019
## link to video
  <https://iiitaphyd-my.sharepoint.com/:v:/g/personal/keshav_bansal_students_iiit_ac_in/EUOMky7OAGdKrPknQiaM7xEBQnE0P4FFbtgAm4GS06RixA?e=KrSkZw>

### Q1: Conversion of NFA to Regex


The algorithm works recursively by splitting an expression into its constituent subexpressions, from which the NFA will be constructed using a set of rules.

More precisely, from a regular expression E, the obtained automaton A with the transition function Δ[clarification needed] respects the following properties:

A has exactly one initial state q0, which is not accessible from any other state. That is, for any state q and any letter a,  does not contain q0.
A has exactly one final state qf, which is not co-accessible from any other state. That is, for any letter a.
Let c be the number of concatenation of the regular expression E and let s be the number of symbols apart from parentheses — that is, |, *, a and ε. Then, the number of states of A is 2s − c (linear in the size of E).
The number of transitions leaving any state is at most two.
Since an NFA of m states and at most e transitions from each state can match a string of length n in time O(emn), a Thompson NFA can do pattern matching in linear time, assuming a fixed-size alphabet.

∈-NFA is similar to the NFA but have minor difference by epsilon move. This automaton replaces the transition function with the one that allows the empty string ∈ as a possible input. The transitions without consuming an input symbol are called ∈-transitions.

In the state diagrams, they are usually labeled with the Greek letter ∈. ∈-transitions provide a convenient way of modeling the systems whose current states are not precisely known: i.e., if we are modeling a system and it is not clear whether the current state (after processing some input string) should be q or q’, then we can add an ∈-transition between these two states, thus putting the automaton in both states simultaneously.

>  while len(ops)>0 and len(ops)!=0:
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









### Q2: NFA to DFA:

For this question I, first calculated the number of states in the NFA and then took all possible combinations of those states which are 2 raised to the power n states. Then for each letter I found out the transition of those states to the different states and thus obtained the tranition matrix for the resulting DFA. The states in the dfa are denoted by lists whereas in the NFA they were in the form of strings. For the final states in DFA if the dfa contains any of the final states of the NFA then it would be a final state. 
Code Snippet:
> for arr in y["states"]:
	for str1 in x["letters"]:
		a=set()
		for str2 in arr:
			for k in range(len(x["transition_matrix"])):
				if x["transition_matrix"][k][0]==str2 and x["transition_matrix"][k][1]==str1:
					a.add(x["transition_matrix"][k][2])



### Q3 Conversion of DFA to regex

For this question, first the Dfa is converted into gnfa by adding one initial and one end state to the dfa using epsilon symbols. All the other states are removed one by one and is replaced by regular expressions by taking union of all the possible paths. After the state is removed all the other remaining pairs which were earlier connected to that state are joined and a regular expression is added at their place. All such combinations are thus generated and finally the regular expression between the two new added states is the required answer.

>  if nfa.remaining_states and a==a:
                    for state2 in nfa.remaining_states:
                        b=state2                        if (state,b) in nfa.transition_table and b==b:

                            reg2 = nfa.transition_table[(m,b)] 

                            if reg2==dol 
                                reg2=''
                            combined_reg =  reg1+self_loop+reg2
                            if combined_reg=='' 
                                combined_reg=dol
                            

                            if (a,b) in nfa.transition_table 
                                q = nfa.transition_table[(a,b)]
                                r="("+q+"+"+combined_reg+")" 
                                nfa.transition_table[(a,b)] = r      

#### Q4 Minimisation of dfa

For this question I implemented the equivalence algorithm for minimisation of dfa.First I divided the states into two sets, one containing the start states and other containing the final states. Then for both sets, starting from the first element , compare it with other states and thus for all such pairs find where the transition lead them to. If it leads them to states which are present in different sets, then, I am putting them in different sets and thus for every set this process is repeated. Finally, we get a new list of lists and we compare it with the old one and if they match then stop the algorithm otherwise continue to run the algorithm.

>  for item2 in x["letters"]:
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
