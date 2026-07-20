class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct = 0
        for i in range(len(nums)):
            if ct==0:
                el = nums[i]
                ct+=1
            elif nums[i]==el:
                ct+=1
            else:
                ct-=1
        return el