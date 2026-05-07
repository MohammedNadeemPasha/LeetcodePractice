
#=============MY CODE================
class TrieNode:
  def __init__(self):
    self.children = {}

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def traverse(self, word: str) -> tuple:
    node = self.root

    for i, letter in enumerate(word):
      if letter in node.children:
        node = node.children[letter]
      else:
        return (node, i)

    return (node, len(word))

  def checkWord(self, word: str) -> tuple:
    node, index = self.traverse(word)

    if index == len(word) and '#' in node.children:
      return (True, node, index)
    else:
      return (False, node, index)

  def addWord(self, word: str) -> bool:
    isWord = self.checkWord(word)

    if isWord[0]:
      return False

    node = isWord[1]
    index = isWord[2]

    for i in range(index, len(word)):
      node.children[word[i]] = TrieNode()
      node = node.children[word[i]]

    node.children['#'] = True
    return True

  def deleteWord(self, word: str) -> bool:
    isWord = self.checkWord(word)

    if not isWord[0]:
      return False

    def recursiveDelete(node, index):
      if index == len(word):
        del node.children['#']
        return len(node.children) == 0

      letter = word[index]
      should_delete = recursiveDelete(node.children[letter], index + 1)

      if should_delete:
        del node.children[letter]

      return len(node.children) == 0

    recursiveDelete(self.root, 0)
    return True

#============== Recommended Code ==================

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    def delete(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                if not node.is_word:
                    return False
                node.is_word = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            child = node.children[char]
            should_delete_child = dfs(child, index + 1)
            if should_delete_child:
                del node.children[char]
                return not node.is_word and len(node.children) == 0
            return False
        dfs(self.root, 0)
        return True