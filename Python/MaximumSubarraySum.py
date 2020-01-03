'''
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''

def maxSequence(arr):
  return 0 if sum(arr) < 0 or arr == [] else sum(arr)



print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# This does not make sense

'''
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

def maxSequence(arr):
  lowest = ans = total = 0
  for i in arr:
    total += i
    lowest = min(lowest, total)
    ans = max(ans, total - lowest)
  return ans


"I think the code complexity is what's important here.
Even though it's not written in the most beatiful way, complexity is very low.

However shadowing the built-in fucntion? definitely not the best practise."

variable shadowing - occurs when a variable declared within a certain scope (decision block, method, or inner class) has the same name as a variable declared in an outer scope.

It’s fine to use shadowing.
You should avoid shadowing by ensuring all names are unique.
You should avoid shadowing by using functions.

'''