class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n
        i = 1
        while(i<n):
            if ratings[i]==ratings[i-1]:
                i+=1
                continue
            peak = 0
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                candies+=peak
                i+=1
            valley = 0
            while i<n and ratings[i]<ratings[i-1]:
                valley+=1
                candies+=valley
                i+=1
            candies-=min(valley,peak)
        return candies