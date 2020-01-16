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
  lines = string.split("\n")

  linesIdx = 0
  for m in markers:
    for l in lines:
      if m in l:
        idx = l.index(m)
        lines[linesIdx] = l[:idx]
        linesIdx += 1
      else:
        lines[linesIdx] = l
        linesIdx += 1
    linesIdx = 0
    idx = 0

  temp = ""
  for l in lines:
    temp += l.strip()
    temp += "\n"

  return temp[:-1]



# try:
#   aa.index("#")
# except ValueError:
#   print("There was a value error")
# else:
#   print("Else block was ran")


# print(aa.index("!"))
# print(aa[10:])

# Replace item in list
# lizt = [1,2,3,4,5]
# lizt[1] = 1
# print(lizt)



print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

# check for new line character



"""
This took 2 days.

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

from re import split, escape


def solution(string, markers):
    if markers:
        pattern = "[" + escape("".join(markers)) + "]"
    else:
        pattern = ''
    return '\n'.join(split(pattern, line)[0].rstrip() for line in string.splitlines())


def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
"""