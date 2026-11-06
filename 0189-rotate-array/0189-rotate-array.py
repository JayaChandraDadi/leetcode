class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        i = 0
        j = n - 1
        while(i<j):
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        nums[k:] = nums[k:][::-1]
        nums[:k] = nums[:k][::-1]
        return nums