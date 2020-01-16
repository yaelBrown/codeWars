"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""

def divisors(int):
  divisor = int
  cnt = int

  out = []

  while cnt > 1:
    if int % divisor == 0:
      out.append(divisor)
    cnt -= 1
    divisor -= 1

  del out[0]
  out.reverse()

  if len(out) == 0:
    return "{} is prime".format(int)
  else:
    return out


# aa = 12

# print(aa,"this is the number:")


print(divisors(13))

empty = []

# print(empty == [])

"""
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)
"""