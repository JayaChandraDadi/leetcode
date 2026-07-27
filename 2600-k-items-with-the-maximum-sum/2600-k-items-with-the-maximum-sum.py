class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        sum1 = 0
        if numOnes>k:
            return k
        sum1+=numOnes
        k-=numOnes
        if numZeros>k:
            return sum1
        k-=numZeros
        if numNegOnes>k:
            sum1-=k
            return sum1
        sum1-=numNegOnes
        return sum1