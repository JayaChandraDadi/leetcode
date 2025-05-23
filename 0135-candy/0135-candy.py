class Solution(object):
    def candy(self, ratings):
        sum1 = 1
        i = 1
        n = len(ratings)
        while(i<n):
            if ratings[i]==ratings[i-1]:
                sum1+=1
                i+=1
                continue
            peak = 1
            while(i<n and ratings[i-1]<ratings[i]):
                peak+=1
                sum1+=peak
                i+=1
            down = 1
            while(i<n and ratings[i-1]>ratings[i]):
                sum1+=down
                i+=1
                down+=1
            if down>peak:
                sum1+=(down-peak)
        return sum1
        