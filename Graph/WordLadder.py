# A transformation sequence from word beginWord to word endWord using a dictionary wordList 
# is a sequence of words:
# beginWord -> s1 -> s2 -> ... -> sk such that:
# - Every adjacent pair of words differs by a single letter.
# - Every si for 1 <= i <= k is in wordList (beginWord does not need to be in wordList).
# - sk == endWord
#
# Given beginWord, endWord, and wordList, return the number of words in the shortest 
# transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
# ex:- beginWord = "hit", endWord = "cog", 
#      wordList = ["hot","dot","dog","lot","log","cog"]; O/P -> 5
#
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"

# ================= My Approach (NOT OPTIMAL BUT WORKS)=================
from typing import List                             
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mapp={}
        seen={}
        self.createNetworkMap(mapp,[beginWord,*wordList])
        q=deque([beginWord])
        seen[beginWord]=True
        result=1
        count=len(q)
        while len(q):
            curr_word=q.popleft()
            if curr_word == endWord:
                return result
            count-=1
            if curr_word in mapp:
                curr_nodes=mapp[curr_word]
                for i in range(len(curr_nodes)):
                    if curr_nodes[i] not in seen:
                        q.append(curr_nodes[i])
                        seen[curr_nodes[i]] = True
            if not count:
                result+=1
                count=len(q)
        return 0

    def createNetworkMap(self,mapp,words):
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                isNeighbour = self.isANeighbour(words[i],words[j])
                if isNeighbour:
                    if words[i] in mapp:
                        mapp[words[i]].append(words[j])
                    else:
                        mapp[words[i]] = [words[j]]
                    if words[j] in mapp:
                        mapp[words[j]].append(words[i])
                    else:
                        mapp[words[j]] = [words[i]]

    def isANeighbour(self,word1,word2):
        diff=1
        if len(word1) != len(word2):
            return False
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                continue
            else:
                diff-=1
                if diff == -1:
                    return False
        return True
sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord, endWord, wordList)) #O/P -> 5
beginWord = "hit"
endWord = "log"
wordList = ["hot","dot","dog","lot","log"]
print(sol.ladderLength(beginWord, endWord, wordList)) #O/P -> 4

# ================= Optimal Approach =================
from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:                         
            return 0

        L = len(beginWord)
        pattern_map = defaultdict(list)
                                                                             # ex- "hot"
        for word in wordList:                                                # pattern_map["*ot"].append("hot")
            for i in range(L):                                               # pattern_map["h*t"].append("hot")  
                pattern = word[:i] + "*" + word[i+1:]                        # pattern_map["ho*"].append("hot")
                pattern_map[pattern].append(word)                            # "*ot" -> ["hot", "dot", "lot"]
                                                                             # "h*t" -> ["hot"]
        q = deque([(beginWord, 1)])                                          # "ho*" -> ["hot"]
        visited = set([beginWord])                                           # "d*t" -> ["dot"]
                                                                             # "do*" -> ["dot", "dog"]
        while q:                                                             # "*og" -> ["dog", "log", "cog"]
            word, steps = q.popleft()                                        

            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]

                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, steps + 1))

                pattern_map[pattern] = []                             # Clearing the already processed node to avoid infinite loop

        return 0
