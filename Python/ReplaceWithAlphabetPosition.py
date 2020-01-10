"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""

def alphabet_position(s):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  out = ""

  for l in s.lower():
    if l.isalpha():
      idx = alphabet.find(l) + 1
      out += str(idx) + " "
      idx = 0
    else:
      pass

  return out.rstrip()

print(alphabet_position("The sunset sets at twelve o' clock."))



"""
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

Could of still imported string, not sure why it was not working before.

from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())
"""