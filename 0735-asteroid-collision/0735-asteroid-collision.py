class Solution(object):
    def asteroidCollision(self, nums):
       st = []
       for i in range(len(nums)):
        if nums[i]>0:
            st.append(nums[i])
        else:
            while st and st[-1]>0 and abs(st[-1])<abs(nums[i]):
                st.pop()
            if st and st[-1]==abs(nums[i]):
                st.pop()
            elif not st or st[-1]<0:
                st.append(nums[i])
       return st