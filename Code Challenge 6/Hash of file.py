# -*- coding: utf-8 -*-
# Hashing is the transformation of a string of characters into a usually shorter fixed-length value or key that represents the original string.
# hashlib - implements a common interface to many different secure hash and message digest algorithms.
# sha1 - Secured Hash Algorithm 1 - a cryptographic hash function which takes an input and -
# produces a 160-bit hash value known as a message digest – typically rendered as a hexadecimal number, 40 digits long.
import hashlib

# storing the hash value of the file
# uniciode objects must be encoded before hashing is a error avoided by b''
# hash.update() is used to add other values in the hash variable
hash_value = hashlib.sha1()
hash_value.update(b'words.txt')

# hash.digest() is used to print the hash value of the file
print("Hash value of the file:", hash_value.digest())
