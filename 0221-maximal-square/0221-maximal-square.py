class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        def findmaxarea(nums):
            n = len(nums)
            st = []
            maxarea = 0
            for i in range(n):
                while st and nums[st[-1]]>nums[i]:
                    nse = i
                    idx = st.pop()
                    if st:
                        pse  = st[-1]
                    else:
                        pse = -1
                    side = min(nums[idx],(nse-pse-1))
                    maxarea = max(maxarea,side*side)
                st.append(i)
            while(st):
                nse = n
                idx = st.pop()
                if st:
                    pse = st[-1]
                else:
                    pse = -1
                side = min(nums[idx],(nse-pse-1))
                maxarea = max(maxarea,side*side)
            return maxarea
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        heights = [0]*n
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j] = 0
            maxarea = max(maxarea,findmaxarea(heights))
        return maxarea