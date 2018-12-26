# -*- coding: utf-8 -*-

# given list
list5 = [1, 3, 6, 78, 35, 55]
list6 = [12, 24, 35, 24, 88, 120, 155]

# Intersection list
Intersect_list = list(set(list5).intersection(set(list6)))
print(Intersect_list)
# output =[35]
