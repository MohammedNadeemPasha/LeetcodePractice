# Given an array of dominoes where dominoes[i] = [a, b],return the number of pairs (i, j) such that i < j and 
# dominoes[i] is equivalent to dominoes[j]. Two dominoes are equivalent if (a == c && b == d) or (a == d && b == c).
# ex:- dominoes = [[1,2],[2,1],[3,4],[5,6]]; O/P -> 1
import math

def dominoPairs(nums):
  d = {}
  for i in range(len(nums)):
    sorted_item = nums[i].sort()
    stringified = "" + str(nums[i][0]) + str(nums[i][1])
    if stringified in d:
      d[stringified] += 1
    else:
      d[stringified] = 1
  result=0
  for i in d:
    if d[i]>1:
      result+=math.comb(d[i],2)
  return result

print(dominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])) #O/P -> 3
print(dominoPairs([[1,2],[2,1],[3,4],[5,6]])) #O/P -> 1