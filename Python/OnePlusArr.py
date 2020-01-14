
"""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
"""

def up_array(l):
  if l == []: return None
  out = ""
  isDoubleDig = False
  for e in l:
    if int(e) > 9: isDoubleDig = True
    out += str(e)

  if "-" in out:
    return None

  if isDoubleDig == True:
    return None

  out = int(out)
  out += 1
  out = str(out)

  outL = []
  for e in out:
    outL.append(int(e))

  return outL

list1 = [2,4,6,8]
list2 = [1, -9]
list3 = [1, 9, 24]


print(up_array(list1))
print(up_array(list2))
print(up_array(list3))

x = lambda x: str(x)


print(type(x(12)))

"""
this kata is stupid.

def up_array(arr):
    return None if arr==[] or any([x not in range(10) for x in arr]) else [int(c) for c in str(int("".join([str(x) for x in arr]))+1)]

def up_array(arr):
    if arr and all(0<=v<=9 for v in arr):
        return map(int, str(int(''.join(map(str,arr)))+1))

def up_array(arr):
    if arr and all(0 <= x <= 9 for x in arr):
        return map(int, str(int(''.join(map(str, arr))) + 1))

def up_array(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
"""