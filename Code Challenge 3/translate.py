# -*- coding: utf-8 -*-
# list containing vowels
vowels_list = list('aeiouAEIOU')

# input string
String4 = input()
String4 = list(String4)

# a list for processing thw operation
repl_list = []

# To translate the string
for var in range(0, len(String4)):
    repl_list.append(String4[var])
    if(String4[var] in vowels_list):
        continue
    elif String4[var] == ' ':
        continue
    else:
        d = repl_list.index(String4[var], len(repl_list)-1)
        repl_list.insert(d+1, 'o')
        repl_list.insert(d+2, String4[var])
repl_list = ''.join(repl_list)
print(repl_list)
# input = This is fun
# output = ToThohisos isos fofunon
