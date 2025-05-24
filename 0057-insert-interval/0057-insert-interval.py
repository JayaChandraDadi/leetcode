class Solution(object):
    def insert(self, intervals, newinterval):
        i = 0
        ans = []
        n = len(intervals)
        while(i<n and intervals[i][1]<newinterval[0]):
            ans.append(intervals[i])
            i+=1
        while(i<n and intervals[i][0]<=newinterval[1]):
            newinterval[0] = min(intervals[i][0],newinterval[0])
            newinterval[1] = max(intervals[i][1],newinterval[1])
            i+=1
        ans.append(newinterval)
        while(i<n):
            ans.append(intervals[i])
            i+=1
        return ans
        