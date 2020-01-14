def longest_palindrome(s):
  sentence = s.split()
  longest = 0

  for w in sentence:
    if w == w[::-1]:
      if len(s) > longest:
        longest = len(w)
    else:
      continue

  return longest

print(longest_palindrome("I like racecars that go fast"))