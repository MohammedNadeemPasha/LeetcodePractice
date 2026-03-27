# There is a new alien language that uses the English lowercase letters, but the order of the letters is unknown.
# You are given a list of words from the alien language’s dictionary, where the words are sorted according to
# the rules of that language. Return a string representing a valid order of characters in the alien language.
# If there are multiple valid answers, return any one of them. If no valid order exists, return "".
# A word a is smaller than word b if at the first position where they differ, the character in a appears before
# the character in b in the alien language. If one word is a prefix of another, then the shorter word must come first.
# ex:- words = ["wrt","wrf","er","ett","rftt"] ; O/P -> "wertf"
#       words = ["z","x"] ; O/P -> "zx"
#       words = ["z","x","z"] ; O/P -> ""
#       words = ["abc","ab"] ; O/P -> ""

# ================= INTUITION=================
# Need to compare the two adjacent words for their first letter difference, and ordering matters; first word's letter come earlier
# than second words letters. Another letter down the line could also share this connection where its difference letter come after 
# the same first words different letter. Hence multiple letters could have a relationship with this first letter, so it should 
# form a graph specifically a directed acyclic graph, for these letters to have a unique relationship, hence to check if thats the case
# we use topological sort.
# ============================================

from collections import defaultdict,deque

def alienDictionary(wordList):
    mapp=defaultdict(list)
    count={}
    for word in wordList:
        for ch in word:
            if ch not in count:
                count[ch] = 0
    for i in range(len(wordList)-1):
        word1=wordList[i]
        word2=wordList[i+1]
        if len(word1) > len(word2) and word1.startswith(word2):
            return ""
        for j in range(min(len(word1),len(word2))):
            if word1[j] != word2[j]:
                if word1[j] not in mapp[word2[j]]:
                    mapp[word2[j]].append(word1[j])
                    count[word1[j]]+=1
                    break
    q=deque()
    for letter in count:
        if count[letter] == 0:
            q.append(letter)
    if not len(q):
        return ""
    result=[]
    while len(q):
        curr_letter=q.popleft()
        result.append(curr_letter)
        for connections in mapp[curr_letter]:
            count[connections]-=1
            if count[connections] == 0:
                q.append(connections)
    if len(result) != len(count):
        return ""
    return "".join(result[::-1])

print(alienDictionary(["wrt","wrf","er","ett","rftt"])) # O/P -> wertf
print(alienDictionary(["ab", "abc"])) # O/P -> cba
print(alienDictionary(["abc", "abx", "abf"])) # O/P -> cxfba