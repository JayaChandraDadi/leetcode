class Solution(object):
    def merge(self,low,mid,high,nums):
        left = low
        right = mid+1
        ct = 0
        temp = []
        while(left<=mid and right<=high):
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while(left<=mid):
            temp.append(nums[left])
            left+=1
        while(right<=high):
            temp.append(nums[right])
            right+=1
        right = mid+1
        for i in range(low,mid+1):
            while(right<=high and nums[i]>2*(nums[right])):
                right+=1
            ct+=(right-mid-1)
        for i in range(low,high+1):
            nums[i] = temp[i-low]
        return ct
    def mergesort(self,low,high,nums):
        ct = 0
        if low>=high:
            return 0
        mid = (low+high)//2
        ct+=self.mergesort(low,mid,nums)
        ct+=self.mergesort(mid+1,high,nums)
        ct+=self.merge(low,mid,high,nums)
        return ct
    def reversePairs(self, nums):
        n = len(nums)
        return self.mergesort(0,n-1,nums)
        
        