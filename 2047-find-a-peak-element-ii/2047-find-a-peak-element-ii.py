class Solution(object):
    def func(self,mat,m,n,mid):
        maxvalue = -1
        index = -1
        for i in range(m):
            if mat[i][mid]>maxvalue:
                maxvalue = mat[i][mid]
                index = i
        return index
    def findPeakGrid(self, mat):
        m = len(mat)
        n = len(mat[0]) if m>0 else 0
        low = 0
        high = n-1
        while(low<=high):
            mid = (low+high)//2
            row = self.func(mat,m,n,mid)
            left = mat[row][mid-1] if mid-1>=0 else -1
            right = mat[row][mid+1] if mid+1<n else -1
            if left<mat[row][mid] and mat[row][mid] > right:
                return [row,mid]
            elif left>=mat[row][mid]:
                high = mid-1
            else:
                low = mid+1
        