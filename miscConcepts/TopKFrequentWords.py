# You are given an array of words and an integer k.
#
# Return the k most frequent words.
# Sort by:
# 1. Higher frequency first
# 2. If same frequency, lexicographically smaller word first
#
# ex:
# words = ["i","love","leetcode","i","love","coding"]
# k = 2
# O/P -> ["i","love"]
#
# Idea:
# - Count frequency of each word using a hashmap.
# - Sort words by:
#   - frequency descending
#   - word ascending
# - Return the first k words.

from collections import defaultdict
import heapq
def topKFrequent( words, k):
    if k==0:
        return []
    freq=defaultdict(int)
    result=[]
    for word in words:
        freq[word]+=1
    word_freq=[]
    for word in freq:
        word_freq.append((-freq[word],word))
    heapq.heapify(word_freq)
    while k>0:
        curr_word=heapq.heappop(word_freq)
        result.append(curr_word[1])
        curr_freq=abs(curr_word[0])
        k-=1
    return result
print(topKFrequent(["i","love","leetcode","i","love","coding"],2)) #O/P -> ['i', 'love']