# Given two words beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences 
# from beginWord to endWord. A transformation sequence is a sequence of words:
# beginWord -> s1 -> s2 -> ... -> sk such that:
# - Every adjacent pair of words differs by exactly one letter.
# - Every si (1 <= i <= k) must exist in wordList.
# - beginWord does not need to be in wordList.
# - sk must be equal to endWord.
# Return all shortest possible sequences, or an empty list if no such sequence exists.
#
# ex:- beginWord = "hit", endWord = "cog", 
#      wordList = ["hot","dot","dog","lot","log","cog"]
# O/P -> [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]]
#
# hit -> hot -> dot -> dog -> cog               =================USE BFS TO FIND THE NODES THAT LEAD TO TARGET =================        
#       |                                       =================THEN USE DFS FROM TARGET TO SOURCE TO TRACE THE PATH=================
#       -> lot -> log -> cog

from collections import defaultdict, deque



def findLadders( beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    L = len(beginWord)
    pattern_map = defaultdict(list)

    for word in wordSet:
        for i in range(L):
            pattern = word[:i] + '*' + word[i+1:]
            pattern_map[pattern].append(word)

    dist = {beginWord: 0}
    parents = defaultdict(list)
    q = deque([beginWord])

    while q:
        word = q.popleft()
        curr_dist = dist[word]

        for i in range(L):
            pattern = word[:i] + '*' + word[i+1:]
            for nei in pattern_map[pattern]:
                if nei not in dist:
                    dist[nei] = curr_dist + 1
                    parents[nei].append(word)
                    q.append(nei)
                elif dist[nei] == curr_dist + 1:
                    parents[nei].append(word)

    if endWord not in dist:
        return []

    res = []
    path = [endWord]

    def dfs(word):
        if word == beginWord:
            res.append(path[::-1])
            return
        for p in parents[word]:
            path.append(p)
            dfs(p)
            path.pop()

    dfs(endWord)
    return res
print(findLadders("hit", "cog",["hot","dot","dog","lot","log","cog"]))