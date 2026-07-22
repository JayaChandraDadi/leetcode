# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def bs(self,low,high,mountainArr,target):
        while(low<=high):
            mid = (low+high)//2
            el = mountainArr.get(mid)
            if el<target:
                low = mid + 1
            elif el>target:
                high = mid - 1
            else:
                return mid
        return -1
    def reversebs(self,low,high,mountainArr,target):
        while(low<=high):
            mid = (low + high)//2
            el = mountainArr.get(mid)
            if target>el:
                high = mid - 1
            elif target<el:
                low = mid + 1
            else:
                return mid
        return -1
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        low = 0
        high = mountainArr.length() - 1
        while(low<high):
            mid = (low + high)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                low = mid + 1
            else:
                high = mid
        peak_idx = low
        ans  = self.bs(0,peak_idx,mountainArr,target) 
        if ans!=-1:
            return ans
        return self.reversebs(peak_idx+1,mountainArr.length()-1,mountainArr,target)
