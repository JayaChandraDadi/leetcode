class Solution:
    def maximumrectangle(self,heights):
        n = len(heights)
        st = []
        maxarea = float('-inf')
        for i in range(n):
            while st and heights[st[-1]]>=heights[i]:
                idx = st.pop()
                nse_idx = i
                if st:
                    pse_idx = st[-1] 
                else:
                    pse_idx = -1
                maxarea = max(maxarea,heights[idx]*(nse_idx-pse_idx-1))
            st.append(i)
        while(st):
            idx = st.pop()
            nse_idx = n
            if st:
                pse_idx = st[-1]
            else:
                pse_idx = -1
            maxarea = max(maxarea,heights[idx]*(nse_idx-pse_idx-1))
        return maxarea
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        maxarea = float('-inf')
        heights = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j] = 0
            maxarea = max(maxarea,self.maximumrectangle(heights))
        return maxarea