# -*- coding: utf-8 -*-

# To extract all the email id having domain gmail
# Importing the regular expression module
import re

# defining the pattern
regex = re.compile("\w+@gmail.com")

# opening the file from where we have to extract value
with open("email.txt", "r") as fileobj:
    data = fileobj.read()

# cleaning the data
data = data.strip()

# searching the data
count = regex.findall(data)

# To print the total mail with particular domain
print("No.of email having domain gmail:", len(count))
