'''
Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
'''

seventeen = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(l):
  count = 0
  for sheep in l:
    if sheep == True:
      count += 1
  return count

print(count_sheeps(seventeen))




'''
There is a count method that would return a number so you dont have to create a output variable

def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
'''