"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(str):
  if str == "": return True
  count = 0
  for p in str:
    if p == "(":
      count+= 1
      print(f"{count} {p}")
    elif p == ")":
      count-= 1
      print(f"{count} {p}")

    if count == -1:
      return False

  return count == 0 # should just do return true




# print(valid_parentheses(")(()))")) # false
# print(valid_parentheses("(())((()())())")) # true
# print(valid_parentheses("hi())(")) # falses
# print(valid_parentheses("hi(hi)(hi)(")) # false
# print(valid_parentheses("m(cq)(()bguixrnhakn)n)whlqg(bngykrjdc)cdplmbp)q")) # false


print(valid_parentheses("())(()"))


"""
directions are vague. Should say if the value of indentation is less than 0, it should immediately be false.

import re

def valid_parentheses(s):
    try:
        re.compile(s)
    except:
        return False
    return True

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string: string = string.replace("()", "")
    return not string

"""