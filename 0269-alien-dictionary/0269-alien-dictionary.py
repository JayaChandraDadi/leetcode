class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        edges = []
        adj = {c:set() for word in words for c in word}
        indegree = {c:0 for word in words for c in word}
        for i in range(1,n):
            w1 = words[i-1]
            w2 = words[i]
            if len(w1)>len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break
        q = deque()
        visited = set()
        for ch in indegree:
            if indegree[ch]==0:
                q.append(ch)
        st = []
        while(q):
            ch = q.popleft()
            st.append(ch)
            for neighbour in adj[ch]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        if len(st)!=len(indegree):
            return ""
        return ''.join(st)


