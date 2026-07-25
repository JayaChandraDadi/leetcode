class Solution:
    def maxProduct(self, n: int) -> int:
        res = []
        while(n!=0):
            rem = n%10
            res.append(rem)
            n = n//10
        maxproduct = 0
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                maxproduct = max(maxproduct,res[i]*res[j])
        return maxproduct