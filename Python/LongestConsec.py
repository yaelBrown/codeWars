"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
"""

def longest_consec(strArr, k):
  if len(strArr) == 0 or k > len(strArr) or k <= 0: return ""
  d = {}
  lengths = []

  for s in strArr:
    d[len(s)] = s
    lengths.append(len(s))

  lengths.sort(reverse=True)
  print(d)

  if k == 1: return d.get(lengths[0])



print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 1))



"""
This somewhat works
"""