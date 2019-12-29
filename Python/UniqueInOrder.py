'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

'''

def unique_in_order(iter):
  if iter == '':
    return []
  lastVal = iter[0]
  out = []
  out.append(lastVal)
  for x in iter:
    if x == lastVal:
      continue
    else:
      out.append(x)
      lastVal = x
  return out

t = 'AAAABBBCCDAABBB'

print(unique_in_order(t))


'''
Could of imported the itertools package.
https://docs.python.org/2/library/itertools.html

from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
'''


# This function will add to list if the value is unique
# def unique_in_order(iter):
#   out = []
#   b = False
#   for item in iter:
#     b = item in out
#     print(b)
#     if b == False:
#       out.append(item)
#     else:
#       continue
#   return out

# t = 'AAAABBBCCDAABBB'

# print(unique_in_order(t)) # [A, B, C, D]