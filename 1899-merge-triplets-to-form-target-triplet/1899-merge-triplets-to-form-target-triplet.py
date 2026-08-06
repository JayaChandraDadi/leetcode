class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [float('-inf')]*3
        for i in range(len(triplets)):
            if triplets[i][0]<=target[0] and triplets[i][1]<=target[1] and triplets[i][2]<=target[2]:
                res[0] = max(res[0],triplets[i][0])
                res[1] = max(res[1],triplets[i][1])
                res[2] = max(res[2],triplets[i][2])
        return res==target