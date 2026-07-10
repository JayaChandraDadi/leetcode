class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = max(citations)
        hindex = 0
        for h in range(n+1):
            ct = 0
            for i in range(len(citations)):
                if ct==h:
                    hindex = h
                    break
                if citations[i]>=h:
                    ct+=1
            if ct==h:
                hindex = h
        return hindex
