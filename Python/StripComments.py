"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def solution(string, markers):
  out = string
  
  for m in markers:
    idx = string.index(m)
    out = out[:idx]

  return out


aa = "this is a # string"

# print(aa.index("#"))
# print(aa[10:])


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

# check for new line character