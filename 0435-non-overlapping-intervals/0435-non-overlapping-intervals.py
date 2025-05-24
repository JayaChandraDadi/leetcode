class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x:x[1])
        freetime = float("-inf")
        ct = 0
        for i in range(len(intervals)):
            if freetime<=intervals[i][0]:
                freetime = intervals[i][1]
                ct+=1
        return len(intervals)-ct

        