# You are given an array of unique words.
#
# Return all words that can be formed by joining at least two shorter words
# from the same array.
#
# ex:
# words = ["cat","cats","catsdogcats","dog","dogcatsdog","rat","ratcatdogcat"]
# O/P -> ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Idea:
# - Store all words in a set for quick lookup.
# - For each word, check if it can be broken into smaller words from the set.
# - Temporarily ignore the word itself so it is not used as the whole answer.
# - Use DFS or DP to try every prefix.
# - If a prefix exists in the set, recursively check the remaining suffix.
# - If the word can be split into at least two valid words, add it to result.
#===========MY Solution(Uses Only recursion and exceeds time limit for 42th test case/43)===============
def wordBreak( s, wordDict):
    result = []
    seen_words = set(wordDict)

    def recursive(i, s, result, acc_string, curr_string, seen_words):
        if curr_string in seen_words:
            if i == len(s):
                acc_string += curr_string
                words = acc_string.split(" ")
                for word in words:
                    if word not in seen_words:
                        return
                result.append(acc_string)
                return

            if i < len(s):
                recursive(i + 1, s, result, acc_string + curr_string + ' ', '' + s[i], seen_words)
                recursive(i + 1, s, result, acc_string, curr_string + s[i], seen_words)
        else:
            if i < len(s):
                recursive(i + 1, s, result, acc_string, curr_string + s[i], seen_words)

    recursive(0, s, result, '', '', seen_words)
    return result

#============== Optimal Solution using DP ===================
def findAllConcatenatedWordsInADict(words):
    root = {}
    for word in words:
        node = root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True
    result = []
    def can_form(word):
        memo = {}
        def dfs(i, node, used):
            state = (i, id(node), used)
            if state in memo:
                return memo[state]
            if i == len(word):
                memo[state] = used and "#" in node
                return memo[state]
            if "#" in node:
                if dfs(i, root, True):
                    memo[state] = True
                    return True
            ch = word[i]
            if ch in node:
                if dfs(i + 1, node[ch], used):
                    memo[state] = True
                    return True
            memo[state] = False
            return False
        return dfs(0, root, False)
    for word in words:
        if can_form(word):
            result.append(word)
    return result
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","rat","ratcatdogcat"])) #O/P->['catsdogcats', 'dogcatsdog', 'ratcatdogcat']