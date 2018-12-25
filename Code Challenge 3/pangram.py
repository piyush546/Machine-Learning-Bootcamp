# -*- coding: utf-8 -*-
# List containing all the alphabets
alphabets = list('abcdefghijklmnopqrstuvwxyz')

# To input the required string
statement = input()


# A function for perfromimg operation on replica state
def operate():
    replica_state = statement.replace(' ', '')
    replica_state = replica_state.replace('.', '')
    replica_state = str.lower(replica_state)
    replica_state = ''.join(set(replica_state))
    replica_state = list(replica_state)
    replica_state = sorted(replica_state)
    return replica_state


# variable for checking true or not and function call
c = 0
replica_state2 = operate()

# To check whether the string is panagram or not
for i in range(0, len(replica_state2)):
    if (replica_state2[i] in alphabets):
        c = c+1
    else:
        continue
if(c == len(alphabets)):
    print("PANAGRAM")
else:
    print("NOT PANAGRAM")
