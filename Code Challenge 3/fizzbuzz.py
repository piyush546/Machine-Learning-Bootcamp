# -*- coding: utf-8 -*-

# program to print fizz for multiple of 3, buzz for multiple of 5 and fizzbuzz for both multiple of 4 and 5
for i in range(1, 51):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 5 == 0):
        print("Buzz")
    elif(i % 3 == 0):
        print("Fizz")
    else:
        print(i)
""" Output :1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz"""