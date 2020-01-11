"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(l):
  out = []
  count = 0
  for x in l:
    if x == 0 and not type(x) == bool:
      count += 1
      continue
    out.append(x)

  if count > 0:
    for y in range(count):
      out.append(0)

  return out



print(move_zeros([False,1,0,1,2,0,1,3,"a"]))


# print(0 == False)