class Solution(object):
    def sumSubarrayMins(self, nums):
        n = len(nums)
        nse = [-1]*(n)
        st = []
        MOD = 10**9+7
        for i in range(n-1,-1,-1):
            while st and nums[i]<nums[st[-1]]:
                st.pop()
            if not st:
                nse[i] = n
            else:
                nse[i] = st[-1]
            st.append(i)
        pse = [-1]*(n)
        st = []
        for i in range(n):
            while st and nums[i]<=nums[st[-1]]:
                st.pop()
            if not st:
                pse[i] = -1
            else:
                pse[i] = st[-1]
            st.append(i)
        total = 0
        for i in range(len(nums)):
            left = i-pse[i]
            right = nse[i]-i
            total=(total+left*right*nums[i])%MOD
        return total
