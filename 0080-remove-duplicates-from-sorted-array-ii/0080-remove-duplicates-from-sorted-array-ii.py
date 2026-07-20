class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1
        ct = 1
        while(i<len(nums)):
            if nums[i]==nums[i-1]:
                ct+=1
                if ct>2:
                    i+=1
                    continue
            else:
                ct = 1
            nums[j] = nums[i]
            i+=1
            j+=1
        return j