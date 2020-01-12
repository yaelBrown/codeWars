"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
import string

def rot13(m):
  out = ""
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase

  for l in m:
    idx = 0
    if not l.isalpha(): 
      out += l
      continue
    elif l.isupper():
      idx = upper.find(l)
      idx += 13
      if idx > 26: idx -= 26
      out += upper[idx]
    elif l.islower():
      idx = lower.find(l)
      idx += 13
      if idx > 26: idx -= 26
      out += lower[idx]
  
  return out

import random

d = ''.join(random.choice(string.ascii_uppercase + string.digits))


print(d)
print(rot13(d))


"""
Says indexeror string index out of range

Traceback (most recent call last):
  File "main.py", line 17, in <module>
    static ("Codewars")
  File "main.py", line 11, in static
    test.assert_equals(rot13(rot13(d)),d)
  File "/home/codewarrior/solution.py", line 25, in rot13
    out += lower[idx]
IndexError: string index out of range


import string
from codecs import encode
import random

sol = lambda s: encode(s, 'rot13')

def static(d):
    test.assert_equals(rot13(d),sol(d))
    test.assert_equals(rot13(rot13(d)),d)

test.describe("rot13 on predefined strings")
static ("test")
static ("test")
static ("Test")
static ("Codewars")
static ("Avoid success at all costs!")
static ("10+2 is twelve.")
static ("abcdefghijklmnopqrstuvwxyz")
test.describe("rot13 on random strings")
for _ in range(100):
    word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    static(word)






"""