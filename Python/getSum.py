'''
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
'''

def get_sum(a,b):
  if a < 0:
    return 0 + b
  elif b < 0:
    return 0 + a
  else:
    if a == b:
      return a
    else:
      return a + b

# print(get_sum(-1,2))


'''
Don't understand how this is the right answer

def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
'''

n = [1,2,3,4,5,6,7,8,9]
print(sum(n)) #45
# print(range(1,10))

# for i in range(10):
#   print(i)

print(sum(2,10)) # int object is not iterable
# range() creates a iterable object


'''
range() - This returns a list of numbers created using range() function.
xrange() - This function returns the generator object that can be used to display numbers only by looping. Only particular range is displayed on demand and hence called “lazy evaluation“.

- If you want to write code that will run on both Python 2 and Python 3, use range() as the xrange funtion is deprecated in Python 3
- range() is faster if iterating over the same sequence multiple times.
- xrange() has to reconstruct the integer object every time, but range() will have real integer objects. (It will always perform worse in terms of memory however)
'''