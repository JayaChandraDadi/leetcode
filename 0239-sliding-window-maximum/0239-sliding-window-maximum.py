from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        st = deque()
        for i in range(k):
            while st and nums[st[-1]]<nums[i]:
                st.pop()
            st.append(i)
        l = 1
        r = k
        ans = []
        ans.append(nums[st[0]])
        while(r<len(nums)):
            while st and nums[st[-1]]<nums[r]:
                st.pop()
            st.append(r)
            if l>st[0]:
                st.popleft()
            ans.append(nums[st[0]])
            l+=1
            r+=1
        return ans