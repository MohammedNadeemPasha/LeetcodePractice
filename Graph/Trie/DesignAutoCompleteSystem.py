# Design an autocomplete system.
#
# For each typed character, return the top 3 historical sentences that start with the current prefix.
#
# Sort suggestions by:
# 1. Higher frequency first
# 2. If same frequency, smaller ASCII order first
#
# When "#" is typed:
# - Save the current sentence into the system.
# - Reset the current input.
# - Return [].
#
# ex:
# sentences = ["i love you", "island", "ironman", "i love leetcode"]
# times = [5, 3, 2, 2]
#
# input("i")
# O/P -> ["i love you", "island", "i love leetcode"]
#
# Idea:
# - Use a Trie to store all sentences.
# - Each Trie node stores children, word-end flag, and frequency.
# - For every input character, update the current prefix.
# - Search the Trie for all sentences starting with that prefix.
# - Use a heap/sort to return the best 3 sentences.
# - When "#" is typed, insert the completed sentence with frequency +1.
# - Then reset the current prefix.

from typing import List
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.frequency = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, freq: int) -> TrieNode:
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.isWord = True
        node.frequency += freq
        return node

    def search(self, prefix: str) -> List[tuple]:
        node = self.root
        result = []

        for letter in prefix:
            if letter not in node.children:
                return []
            node = node.children[letter]

        def dfs(node, sentenceSoFar):
            if node.isWord:
                result.append((-node.frequency, sentenceSoFar))

            for letter in node.children:
                dfs(node.children[letter], sentenceSoFar + letter)

        dfs(node, prefix)
        return result


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.enteredCharacter = ""
        self.count = 1
        self.valid_sentences = []

        self.addWords(sentences, times)

    def addWords(self, sentences: List[str], times: List[int]) -> None:
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])

    def topThreeSentences(self) -> List[str]:
        self.valid_sentences = [
            item for item in self.valid_sentences
            if item[1].startswith(self.enteredCharacter)
        ]

        temp = self.valid_sentences[:]
        heapq.heapify(temp)

        result = []
        for _ in range(3):
            if temp:
                result.append(heapq.heappop(temp)[1])

        return result

    def input(self, char: str) -> List[str]:
        if char == "#":
            self.trie.insert(self.enteredCharacter, 1)
            self.enteredCharacter = ""
            self.count = 1
            self.valid_sentences = []
            return []

        self.enteredCharacter += char

        if self.count:
            self.valid_sentences = self.trie.search(self.enteredCharacter)
            self.count -= 1

        return self.topThreeSentences()
obj = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
print(obj.input("i"))
# ["i love you", "island", "i love leetcode"]
print(obj.input(" "))
# ["i love you", "i love leetcode"]
print(obj.input("a"))
# []
print(obj.input("#"))
# []