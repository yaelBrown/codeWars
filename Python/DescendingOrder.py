"""
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

def descending_order(n):
  out = [str(x) for x in str(n)]
  out.sort(reverse=True)

  return int("".join(out))




print(descending_order(123456789))




"""
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

easy to read... lol @ :

def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)

"""