# -*- coding: utf-8 -*-
# Hashing is the transformation of a string of characters into a usually shorter fixed-length value or key that represents the original string.
# hashlib - implements a common interface to many different secure hash and message digest algorithms.
# sha1 - Secured Hash Algorithm 1 - a cryptographic hash function which takes an input and -
# produces a 160-bit hash value known as a message digest – typically rendered as a hexadecimal number, 40 digits long.
import hashlib

with open("words.txt", "r") as fileobj:
    words = fileobj.read().splitlines()

# storing the hash value of the file
# uniciode objects must be encoded before hashing is a error avoided by b''if using update
# hash.update() is used to add other values in the hash variable
# hash.digest() is used to print the hash value of the string
# hash.hexdigest() is used to print the hex hash value of the string
# using encode for avoiding use of update as it will only accept byte values

# list holding hash of the words
hash_words = []

# getting the hash values of the words in the file
for var in words:
    hash_value = hashlib.sha1(var.encode('utf-8')).digest()
    hash_words.append(hash_value)

# Making a new file containing the hash of the words in words.txt file
# Using wb method as w have to write byte value in the file
with open("hashwords.txt", "wb") as fileobj:
    for var2 in range(0, len(hash_words)):
        fileobj.write(hash_words[var2]+"\n".encode('utf-8'))
