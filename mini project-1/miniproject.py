# -*- coding: utf-8 -*-
# .replace in str have count which specify how much occurence of particular character is to be replaced
# str has function .find() to get the index position of a particular substring same as index but it give -1 if not found
# whereas index give ValueError
# .start() is used to get the index returned by search in regex
# Mini project using sets, regex, File handling

import re

regex = re.compile("START OF")
regex2 = re.compile("END OF")
regex3 = re.compile("[a-zA-Z]+")


# function for getting the words in a particular novel
def novel_filter(novel_name):
    with open(novel_name, "r", encoding="utf-8") as fileobj:
        data = fileobj.read()
        result = regex.search(data).start()
        startindex = data.find("\n", result)
        result = regex2.search(data).start()
        data = data[startindex:result].split()
    final_list = []
    for var in range(0, len(data)):
        final_list.extend(regex3.findall(data[var]))
    print("Number of words:", len(final_list))
    print("Unique words:", len(set(final_list)))
    return set(final_list)


# Function calls
set1 = novel_filter("james_joyce_ulysses.txt")
set2 = novel_filter("moby_dick_melville.txt")
set3 = novel_filter("robinson_crusoe_defoe.txt")
set4 = novel_filter("sons_and_lovers_lawrence.txt")
set5 = novel_filter("the_way_of_all_flash_butler.txt")
set6 = novel_filter("to_the_lighthouse_woolf.txt")
set7 = novel_filter("metamorphosis_kafka.txt")

# For finding common words and the words that are only in set1
repl_set = [set2, set3, set4, set5, set6, set7]
common_words = set(set.intersection(set1, *repl_set))
unique_words = set1 - set(common_words)
