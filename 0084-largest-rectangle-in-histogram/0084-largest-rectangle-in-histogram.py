class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        maxarea = float('-inf')
        for i in range(n):
            while(st and heights[st[-1]]>=heights[i]):
                idx = st.pop()
                nse = i
                if st:
                    pse = st[-1]
                else:
                    pse = -1
                maxarea = max(maxarea,heights[idx]*(nse-pse-1))
            st.append(i)
        while(st):
            idx = st.pop()
            nse = n
            if st:
                pse = st[-1]
            else:
                pse = -1
            maxarea = max(maxarea,heights[idx]*(nse-pse-1))
        return maxarea