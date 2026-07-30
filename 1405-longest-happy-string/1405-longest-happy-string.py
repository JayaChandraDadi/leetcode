import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a>0:
            heapq.heappush(pq,(-a,'a'))
        if b>0:
            heapq.heappush(pq,(-b,'b'))
        if c>0:
            heapq.heappush(pq,(-c,'c'))
        ans = []
        while(pq):
            freq1,ch1 = heapq.heappop(pq)
            blocked = False
            if len(ans)>=2 and ans[-1]==ch1 and ans[-2]==ch1:
                blocked = True
            if blocked:
                if not pq:
                    break
                freq2,ch2 = heapq.heappop(pq)
                ans.append(ch2)
                freq2+=1
                if freq2<0:
                    heapq.heappush(pq,(freq2,ch2))
                heapq.heappush(pq,(freq1,ch1))
            else:
                ans.append(ch1)
                freq1+=1
                if freq1<0:
                    heapq.heappush(pq,(freq1,ch1))
        return ''.join(ans)