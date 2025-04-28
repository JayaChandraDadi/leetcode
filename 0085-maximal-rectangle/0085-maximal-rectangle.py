class Solution(object):
    def maxrectangle(self,arr):
        n = len(arr)
        st = []
        maxarea = 0
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                el = st.pop()
                nse = i
                pse = st[-1] if st else -1
                maxarea = max(maxarea,(arr[el])*(nse-pse-1))
            st.append(i)
        while st:
            el = st.pop()
            nse = n
            pse = st[-1] if st else -1
            maxarea = max(maxarea,(arr[el])*(nse-pse-1))
        return maxarea
    def maximalRectangle(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        maxi = 0
        presum = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            sum1 = 0
            for i in range(m):
                if int(matrix[i][j])==0:
                    sum1 = 0
                else:
                    sum1+=int(matrix[i][j])
                presum[i][j] = sum1
        for i in range(m):
            maxi = max(maxi,self.maxrectangle(presum[i]))
        return maxi


        