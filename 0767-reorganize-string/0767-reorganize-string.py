import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = {}
        n = len(s)
        pq = []
        for i in range(n):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            hashmap[s[i]]+=1
            if hashmap[s[i]]>(n+1)//2:
                return ''
        ans = ''
        for ch,ct in hashmap.items():
            heapq.heappush(pq,(-ct,ch))
        while(pq):
            freq1,ch1 = heapq.heappop(pq)
            freq1 = abs(freq1)
            if freq1==0:
                continue
            if pq and ans and ans[-1]==ch1:
                freq2,ch2 = heapq.heappop(pq)
                freq2 = abs(freq2)
                if freq2==0:
                    continue
                ans+=ch2
                freq2-=1
                heapq.heappush(pq,(-freq2,ch2))
            ans+=ch1
            freq1-=1
            heapq.heappush(pq,(-freq1,ch1))
        return ans