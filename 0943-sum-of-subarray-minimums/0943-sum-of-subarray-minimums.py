class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        nse = [-1]*n
        pse = [-1]*n
        st = []
        total = 0
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
        for i in range(n):
            left = i-pse[i]
            right = nse[i] - i
            total=(total+left*right*arr[i])%((10**9)+7)
        return total

            
