class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        i = 0
        j = n//2
        ans = []
        while(j<n):
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j+=1
        return ans