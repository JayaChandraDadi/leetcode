class Solution:
    def canSeePersonsCount(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        st = []
        for i in range(n-1,-1,-1):
            ct = 0
            while st and st[-1]<nums[i]:
                st.pop()
                ct+=1
            if st:
                ct+=1
            st.append(nums[i])
            ans.append(ct)
        return ans[::-1]