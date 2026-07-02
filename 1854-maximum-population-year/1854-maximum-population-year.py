class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        hashmap = {}
        for birth,death in logs:
            if birth not in hashmap:
                hashmap[birth] = 0
            hashmap[birth]+=1
            if death not in hashmap:
                hashmap[death] = 0
            hashmap[death]-=1
        maxct = float('-inf')
        sum1 = 0
        for year in sorted(hashmap.keys()):
            sum1+=hashmap[year]
            if sum1>maxct:
                maxct = sum1
                ans = year
        return ans