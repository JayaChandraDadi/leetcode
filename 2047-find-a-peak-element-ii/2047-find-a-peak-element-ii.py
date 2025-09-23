class Solution(object):
    def findmax(self,mat,m,n,mid):
        max1 = float('-inf')
        for i in range(m):
            if mat[i][mid]>max1:
                max1 = mat[i][mid]
                maxrow = i
        return maxrow
    def findPeakGrid(self, mat):
       m = len(mat)
       n = len(mat[0]) if m else 0
       low = 0
       high = n-1
       while(low<=high):
        mid = (low+high)//2
        maxrow = self.findmax(mat,m,n,mid)
        left = mat[maxrow][mid-1] if mid-1>=0 else -1
        right = mat[maxrow][mid+1] if mid+1<n else 0
        if left<mat[maxrow][mid]>right:
            return [maxrow,mid]
        elif left>=mat[maxrow][mid]:
            high = mid-1
        else:
            low = mid+1
       return -1