class Solution(object):
    def findmax(self, nums):
        n = len(nums)
        st = []
        maxarea = float('-inf')
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                el = st.pop()
                nse = i
                pse = st[-1] if st else -1
                maxarea = max(maxarea,(nse-pse-1)*nums[el])
            st.append(i)
        while st:
            el = st.pop()
            nse = n
            pse = st[-1] if st else -1
            maxarea = max(maxarea,(nse-pse-1)*nums[el])
        return maxarea
    def maximalRectangle(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        premat = [[0]*n for _ in range(m)]
        for i in range(m):
            presum = 0
            for j in range(n):
                if matrix[i][j]==0:
                    premat[i][j] = 0
                else:
                    premat[i][j] = int(matrix[i][j])+(int(premat[i-1][j]) if i>0 else 0)
        maxarea = float('-inf')
        for i in range(m):
            maxarea = max(maxarea,self.findmax(premat[i]))
        return maxarea


        