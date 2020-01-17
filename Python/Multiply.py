"""
Fix multiply and create tests
"""

import string

def multiply(a, b):
  def mulHelper(z):
    if type(z) == int or type(z) == float:
      return True
    else:
      return False

  if mulHelper(a) and mulHelper(b):
    return a * b
  else:
    return "Please enter numbers"



# test.assert_equals(multiply(2,3), 6)
# test.assert_equals(multiply(2,"cookies"), "Please enter numbers")


print(type(1.5))

print(multiply(1.5, 2.5))



print(str(1.5).isdigit())