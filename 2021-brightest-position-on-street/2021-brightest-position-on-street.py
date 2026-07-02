class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        n = len(lights)
        hashmap = {}
        for i in range(n):
            position = lights[i][0]
            range1 = lights[i][1]
            lights[i][0] = position - range1
            lights[i][1] = position + range1
        for start,end in lights:
            if start not in hashmap:
                hashmap[start] = 0
            hashmap[start]+=1
            if end+1 not in hashmap:
                hashmap[end+1] = 0
            hashmap[end+1]-=1
        sum1 = 0
        for point in sorted(hashmap.keys()):
            sum1+=hashmap[point]
            hashmap[point] = sum1
        maxct = float('-inf')
        for point in sorted(hashmap.keys()):
            ct = hashmap[point]
            if ct>maxct:
                maxct = ct
                ans = point
        return ans