"""

Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters

"""
import string

def kebabize(string):
  out = ""
  for l in string:
    if not l.isalpha():
      continue
    elif l.isupper():
      out += "-"
      out += l
    else:
      out += l
  
  if out == "": return out
  if out[0] == "-": out = out[1:]

  return out.lower()

# aa = "this is a string"
# print(aa.isalpha())




# print(kebabize("iLike4Cookies"))

# print("-S-O-S"[:1])

print(kebabize("SOS"))



"""
def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

import re

def kebabize(s):
    return re.sub('\B([A-Z])', r'-\1', re.sub('\d', '', s)).lower()

import re
def kebabize(s):
    s = ''.join([i for i in s if not i.isdigit()])
    kebablist = filter(None, re.split("([A-Z][^A-Z]*)", s))
    return "-".join(x.lower() for x in kebablist)

"""
