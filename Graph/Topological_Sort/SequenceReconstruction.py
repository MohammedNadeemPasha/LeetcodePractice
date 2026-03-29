# Given an original sequence org and a list of sequences seqs, return true if org can be uniquely reconstructed.
# The reconstruction means building the shortest common supersequence such that all sequences in seqs
# are subsequences of it, and there is exactly one valid reconstruction equal to org.
# ex:- org = [1,2,3], seqs = [[1,2],[1,3]] ; O/P -> false
# Explanation:
# From seqs, multiple valid sequences can be formed (e.g., [1,2,3] and [1,3,2]), so the reconstruction is not unique.

#==============My Solution============
from collections import defaultdict,deque
def SequenceReconstruction(org,seq):
    if not len(seq):
        return False
    
    mapp=defaultdict(set);q=deque();count=defaultdict(int);result=[]

    for i in range(len(seq)):
        if len(seq[i])==1 and seq[i][0] not in count:
            count[seq[i][0]]=0
            continue
        for j in range(1,len(seq[i])):
            if seq[i][j-1] not in mapp[seq[i][j]]:
                mapp[seq[i][j]].add(seq[i][j-1])
                count[seq[i][j-1]]+=1
            if seq[i][j] not in count:
                count[seq[i][j]]=0
    
    for nodes in count:
        if count[nodes] == 0:
            q.append(nodes)
            result.append(nodes)
    if not len(q):
        return False
    print(q,mapp,count)
    while len(q):
        if len(q)>1 :
            return False
        curr_node=q.popleft()
        for i in mapp[curr_node]:
            count[i]-=1
            if count[i] ==0:
                result.append(i)
                q.append(i)
    reversedresult=result[::-1]
    if len(org) != len(reversedresult):
        return False
    for i in range(len(reversedresult)):
        if reversedresult[i] == org[i]:
            continue
        else:
            return False
    return True

print(SequenceReconstruction([1,2,3],[[1,2],[2,4]])) # O/P -> False

#=============Better readable code============
from collections import defaultdict, deque

def SequenceReconstruction(org, seqs):
    if not org:
        return not seqs

    graph = defaultdict(set)
    indegree = {x: 0 for x in org}
    seen = set()

    for seq in seqs:
        for num in seq:
            if num not in indegree:
                return False
            seen.add(num)

        for i in range(1, len(seq)):
            prev, curr = seq[i - 1], seq[i]
            if curr not in graph[prev]:
                graph[prev].add(curr)
                indegree[curr] += 1

    if seen != set(org):
        return False

    q = deque([x for x in org if indegree[x] == 0])
    result = []

    while q:
        if len(q) > 1:
            return False

        node = q.popleft()
        result.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return result == org