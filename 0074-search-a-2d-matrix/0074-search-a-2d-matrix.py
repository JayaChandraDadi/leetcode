class Solution(object):
    def search(self,arr,x,n):
        low = 0
        high = n-1
        while(low<=high):
            mid = (low+high)//2
            if arr[mid]<x:
                low = mid+1
            elif arr[mid]>x:
                high = mid-1
            else:
                return 1
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0]) if m>0 else 0
        for i in range(m):
            k = self.search(matrix[i],target,n)
            if k==1:
                return True
        return False
        