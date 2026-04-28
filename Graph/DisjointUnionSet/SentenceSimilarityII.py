from collections import defaultdict
def sentenceSimilarity(word1,word2,pairs):
    if len(word1) != len(word2):
        return False
    parent=defaultdict(str)
    for i in range(len(word1)):
        parent[word1[i]]=word1[i]
        parent[word2[i]]=word2[i]
    def find(x):
        if parent[x] != x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        rootX=find(x)
        rootY=find(y)
        if rootX != rootY:
            parent[rootX]=rootY
        
    for pair in pairs:
        x,y=pair
        if x not in parent:
            parent[x]=x
        if y not in parent:
            parent[y]=y
        union(x,y)
    for i in range(len(word2)):
        if find(word2[i]) != find(word1[i]):
            return False
    return True

print(sentenceSimilarity(["great", "acting", "skills"],["fine", "drama", "talent"],[["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]])) # O/P -> True
print(sentenceSimilarity(['great'],['greate'],[])) # O/P -> False
print(sentenceSimilarity(['great'],['beat'],[['reset','great']])) # O/P -> False