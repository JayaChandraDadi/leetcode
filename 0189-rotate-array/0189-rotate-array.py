class Solution(object):
    def rotate(self, arr, k):
        n = len(arr)
        k = (k)%(n)
        temp = []
        for i in range(n-k,n):
            temp.append(arr[i])
        for i in range(n,k,-1):
            arr[i-1] = arr[i-k-1]
        for i in range(k):
            arr[i] = temp[i]