# Problem:- Given an integer array arr, you start at index 0. In one step you can move to:
# 1) i + 1 if it is within bounds
# 2) i - 1 if it is within bounds
# 3) any index j where arr[i] == arr[j] and i != j
# Return the minimum number of steps required to reach the last index of the array.
# Ex:- arr = [100,-23,-23,404,100,23,23,23,3,404]  ->  O/P: 3

from collections import deque

def minJumps(arr):
    dp=[float('inf')]*len(arr)
    dp[0]=0
    seen={}
    for i in range(len(arr)):
        if arr[i] in seen:
            seen[arr[i]].append(i)
        else:
            seen[arr[i]]=[i]
    q=deque()
    q.append([arr[0],0,0])
    while(len(q)):
        curr_elem,curr_index,curr_value=q.popleft()
        if curr_elem in seen:
            for i in range(len(seen[curr_elem])):
                index= seen[curr_elem][i]
                if dp[index] > curr_value+1:
                    dp[index]= curr_value+1
                    q.append([arr[index],index,dp[index]])
            del seen[curr_elem]
        if curr_index-1 >=0:
            if dp[curr_index-1]>curr_value+1:
                dp[curr_index-1] = curr_value+1
                q.append([arr[curr_index-1],curr_index-1,dp[curr_index-1]])
        if curr_index+1<=len(arr)-1:
            if dp[curr_index+1] > curr_value+1:
                dp[curr_index+1] = curr_value+1
                q.append([arr[curr_index+1],curr_index+1,dp[curr_index+1]])
    return dp[len(arr)-1]

print(minJumps([100,-23,-23,404,100,23,23,23,3,404])) #O/P -> 3
print(minJumps([7])) # O/P -> 0
print(minJumps([7,6,9,6,9,6,9,7])) #O/P -> 1