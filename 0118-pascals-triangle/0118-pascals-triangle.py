class Solution(object):
    def generate(self, n):
        def ncr(n,r):
            res = 1
            for i in range(r):
                res = (res*(n-i))//(i+1)
            return res
        ans = []
        for row in range(1,n+1):
            temp = []
            for col in range(1,row+1):
                temp.append(ncr(row-1,col-1))
            ans.append(temp)
        return ans