"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""
import re

def reverse_words(t):
  re_S = re.compile(r'(\S+)')
  temp = re_S.split(t)
  out = []

  for w in temp:
    out.append(w[::-1])

  return "".join(out)




test = "test     string"
re_S = re.compile(r'(\S+)')

# print(re_S.split(test))


print(test.split(" "))

print(reverse_words("double  spaces"))

# print(test[::-1])





"""
re library is regular expressions.

--
def reverse_words(str):
  return ' '.join(s[::-1] for s in str.split(' '))

--
import re

def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)


--
def reverse_words(str):
  return " ".join(map(lambda word: word[::-1], str.split(' ')))
"""