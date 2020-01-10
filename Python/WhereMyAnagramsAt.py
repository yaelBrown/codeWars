"""
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

def anagrams(w, l):
  out = []
  contains = True
  for letter in w:
    for x in l:
      if x.find(letter) == -1:
        contains = False

      if contains == True:
        out.append(x)
      else:
        contains = True
  return out



# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada', ]))


testL = ['aabb', 'abcd', 'bbaa', 'dada', ]

w = 'abba'
# sort the words, they are equal
print(sorted('racer'))
print(sorted('carer'))

"""
solutions:

sort the words, then compare them. If they are equal they are anagrams because they contain the same letters, nothing more nothing less.

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)
"""