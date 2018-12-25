# -*- coding: utf-8 -*-
# List containing the vowels and the states
list1 = ['a', 'e', 'i', 'o', 'u']
state_name = ['Alabama', 'California', 'Oklahoma', 'Florida']

# Process to remove the vowels
for i in range(0, len(state_name)):
    replica_state = str.lower(state_name[i])
    replica_state = list(replica_state)
    d = len(state_name[i])
    for j in range(0, d):
        if (replica_state[j] in list1):
            replica_state[j] = ''
        else:
            continue
    replica_state = ''.join(replica_state)
    state_name[i] = str.capitalize(replica_state)

# printing the modified list
print("Modified list:", state_name)

# Output = Modified list: ['Lbm', 'Clfrn', 'Klhm', 'Flrd']
