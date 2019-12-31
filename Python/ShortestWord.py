'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

def find_short(s):
  words = s.split(" ")
  shortest = 189820
  for w in words:
    if len(w) < shortest:
      shortest = len(w)
  return shortest

print(find_short("bitcoin take over the world maybe who knows perhaps"))