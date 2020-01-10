"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

import string

def is_pangram(s):
  temp = []

  for l in s.lower():
    if (l in string.ascii_lowercase) and l != " " and (l not in temp):
      temp.append(l)

  temp.sort()
  temp = "".join(temp)

  return temp == string.ascii_lowercase

pangram = "The quick, brown fox jumps over the lazy dog!"


# print(is_pangram(pangram))
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ")) # should be true

testL = ["a", "b", "c"]

# print("d" not in testL)


print(string.ascii_lowercase)


"""
A lot of googling for this one.

learn sets !

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())


def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.lowercase)


def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
"""