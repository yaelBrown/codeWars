"""
We want to create a function that will add numbers together when called in succession.

add(1)(2);
// returns 3
We also want to be able to continue to add numbers to our chain.

add(1)(2)(3); // 6
add(1)(2)(3)(4); // 10
add(1)(2)(3)(4)(5); // 15
and so on.

A single call should return the number passed in.

add(1); // 1
We should be able to store the returned values and reuse them.

var addTwo = add(2);
addTwo; // 2
addTwo + 5; // 7
addTwo(3); // 5
addTwo(3)(5); // 10
We can assume any number being passed in will be valid whole number.
"""
from functools import partial


def curry(fnc):
  def inner(arg):
    if len(signature(fnc).parameters) == 1:
      return fnc(arg)
    return curry(partial(fnc, arg))
  return inner

@curry
def add(a,b):
  return a+b


# print(add(1)(2)(3))



# https://github.com/PacktPublishing/Functional-Programming-in-7-Days/blob/master/Section%207/7.1%20Currying%20in%20Python%203.ipynb
from inspect import signature

# Create a decorator
def curry_func(my_func):

    # define inner function
    def inner_wrap(args):

        # Check no. of paramters in function signature
        if len(signature(my_func).parameters) == 1:
            return my_func(args)

        # If more than 1 paramter recursively apply
        # the decorator and call partial
        else:
            return curry_func(partial(my_func, args))

    return inner_wrap

"""
This is called currying
https://www.codewars.com/kata/539a0e4d85e3425cb0000a88
"""