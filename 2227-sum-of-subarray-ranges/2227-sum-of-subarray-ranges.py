class Solution(object):
    def subArrayRanges(self, nums):
        n = len(nums)
        st = []
        pse = [-1]*n
        pge = [-1]*n
        nge = [-1]*n 
        nse = [-1]*n
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if not st:
                nge[i] = n
            else:
                nge[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>nums[i]:
                st.pop()
            if not st:
                nse[i] = n
            else:
                nse[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n):
            while st and nums[st[-1]]<nums[i]:
                st.pop()
            if not st:
                pge[i] = -1
            else:
                pge[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                pse[i] = -1
            else:
                pse[i] = st[-1]
            st.append(i)
        leftrange =0
        rightrange = 0
        for i in range(n):
            leftmin = i-pse[i]
            rightmin = nse[i]-i
            leftmax = i-nge[i]
            rightmax = pge[i]-i
            leftrange+=(leftmin*rightmin*nums[i])
            rightrange+=(leftmax*rightmax*nums[i])
        return rightrange-leftrange
        