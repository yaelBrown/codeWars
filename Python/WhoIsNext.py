"""
Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
Write a program that will return the name of the person who will drink the n-th cola.

Input
The input data consist of an array which contains at least 1 name, and single integer n which may go as high as the biggest number your language of choice supports (if there's such limit, of course).

Output / Examples
Return the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1.

who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"
"""

def win(names, r):
  temp = ""
  cnt = 1

  while cnt != r:
    temp = names[0]
    names.pop(0)
    names.append(temp)
    names.append(temp)
    cnt += 1

  return names[0]








def who_is_next(names, r):
  if r == 0: return names[0]
  l = []
  d = {}
  cnt = 1

  for n in names:
    d[n] = 1

  idx = 0

  if r < len(names):
    return names[r - 1]

  while cnt != r:
    d[names[0]] *= 2
    cnt += 1
    names.append(names[0])
    names.pop(0)
    idx += 1

    if idx == len(names): idx = 0

  print()

  return d

print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52))
print(win(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52))




"""
This works, but not with big numbers

  # while cnt != r:
  #   temp = names[0]
  #   names.pop(0)
  #   names.append(temp)
  #   names.append(temp)
  #   cnt += 1

a,a,a,a,b,b,b,b,c,c,c,c

"""