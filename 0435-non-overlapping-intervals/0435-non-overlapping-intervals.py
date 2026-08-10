class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x:x[1])
        ct = 0
        curr_end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<curr_end:
                ct+=1
            else:
                curr_end = intervals[i][1]
        return ct