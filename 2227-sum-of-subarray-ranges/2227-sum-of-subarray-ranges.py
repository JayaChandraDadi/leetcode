class Solution(object):
    def subArrayRanges(self, arr):
        n = len(arr)
        nse = [-1]*n
        pse = [-1]*n
        st = []
        nge = [-1]*n
        pge = [-1]*n
        totalmin = 0
        totalmax = 0
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            else:
                nse[i] = n
            st.append(i)
        st = []
        for i in range(n):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                pse[i] = st[-1]
            else:
                pse[i] = -1
            st.append(i)
        st = []
        for i in range(n):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            if st:
                pge[i] = st[-1]
            else:
                pge[i] = -1
            st.append(i)
        st = []
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]<arr[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            else:
                nge[i] = n
            st.append(i)
        for i in range(n):
            leftmin = i-pse[i]
            rightmin = nse[i] - i
            leftmax = i - pge[i]
            rightmax = nge[i] - i
            totalmin+=(leftmin*rightmin*arr[i])
            totalmax+=(leftmax*rightmax*arr[i])
        return totalmax-totalmin

        
        