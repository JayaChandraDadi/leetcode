
class Solution(object):
    def merge(self, a, low, mid, high):
        ct = 0
        left = low
        right = mid+1
        j = mid+1
        temp = []
        while(left<=mid and right<=high):
            if a[left]<=a[right]:
                temp.append(a[left])
                left+=1
            else:
                temp.append(a[right])
                right+=1
        while(left<=mid):
            temp.append(a[left])
            left+=1
        while(right<=high):
            temp.append(a[right])
            right+=1
        for i in range(low,mid+1):
            while(j<=high and a[i]>(2*a[j])):
                j+=1
            ct+=(j-mid-1)
        for i in range(low,high+1):
            a[i] = temp[i-low]
        return ct
    def mergesort(self,a,low,high):
        cnt = 0
        if low==high:
            return cnt
        mid = (low+high)//2
        cnt+=self.mergesort(a,low,mid)
        cnt+=self.mergesort(a,mid+1,high)
        cnt+=self.merge(a,low,mid,high)
        return cnt

    def reversePairs(self, nums):
        n = len(nums)
        return self.mergesort(nums,0,n-1)
        