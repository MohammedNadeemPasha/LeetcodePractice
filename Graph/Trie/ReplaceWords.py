# You are given a dictionary of root words and a sentence.
# Replace each word in the sentence with the shortest root that is its prefix.
# If no root matches, keep the word unchanged.
#
# ex:
# dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
# O/P -> "the cat was rat by the bat"
#
# Idea:
# - Store all roots in a Trie.
# - For each word in the sentence:
#   - Search the Trie character by character.
#   - If a root ends during the search, replace the word with that root.
#   - Because we check from left to right, the first root found is the shortest.
#   - If no root is found, keep the original word.
# - Join all processed words back into a sentence.
#========= My Solution=========
def replaceWords( dictionary, sentence) :
    roots = set(dictionary)
    result = []
    for word in sentence.split():
        replacement = word
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix in roots:
                replacement = prefix
                break
        result.append(replacement)
    return " ".join(result)
print(replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery")) #O/P->the cat was rat by the bat
