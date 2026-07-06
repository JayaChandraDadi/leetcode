class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        ans = []
        ans.append(intervals[0])
        for i in range(1,n):
            if intervals[i][0]>=ans[-1][0] and intervals[i][1]<=ans[-1][1]:
                continue
            elif intervals[i][0]<=ans[-1][0] and intervals[i][1]>=ans[-1][1]:
                ans.pop()
            ans.append(intervals[i])
        return len(ans)
