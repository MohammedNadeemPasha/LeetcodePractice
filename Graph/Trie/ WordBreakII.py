# You are given a string s and a dictionary wordDict.
#
# Return all possible sentences by adding spaces so that
# every word is in wordDict.
# Words can be reused multiple times.
#
# ex:
# s = "catsanddog"
# wordDict = ["cat","cats","and","sand","dog"]
# O/P -> ["cats and dog", "cat sand dog"]
#
# Idea:
# - Use DFS/backtracking to try every possible word starting at each index.
# - If a prefix is in wordDict, recursively solve the remaining string.
# - Use memoization so each index is solved only once.
# - Base case: if index reaches the end of s, return one empty sentence.
# - Combine the current word with each sentence from the recursive result.
# - Return all complete sentences.

#================ My Solution ==================
def wordBreak( s, wordDict) :
    result=[]
    seen_words=set(wordDict)
    def recursive(i,s,result,acc_string,curr_string,seen_words):
        if curr_string in seen_words:
            if i==len(s):
                acc_string+=curr_string
                words=acc_string.split(" ")
                for word in words:
                    if word not in seen_words:
                        return
                result.append(acc_string)
                return
            if i <len(s):
                recursive(i+1,s,result,acc_string+curr_string+' ',''+s[i],seen_words)
                recursive(i+1,s,result,acc_string,curr_string+s[i],seen_words)
        else:
            if i<len(s):
                recursive(i+1,s,result,acc_string,curr_string+s[i],seen_words)
    recursive(0,s,result,'','',seen_words)
    return result
#================DP Based SOlution ===================
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return [""]

            res = []

            for word in words:
                if s.startswith(word, i):
                    suffixes = dfs(i + len(word))

                    for suffix in suffixes:
                        if suffix:
                            res.append(word + " " + suffix)
                        else:
                            res.append(word)

            memo[i] = res
            return res

        return dfs(0)