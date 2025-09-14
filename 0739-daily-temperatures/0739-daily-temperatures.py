class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        nge = [-1]*n
        st = []
        for i in range(len(temperatures)-1,-1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if not st:
                nge[i] = 0
            else:
                nge[i] = st[-1]-i 
            st.append(i)
        return nge

        