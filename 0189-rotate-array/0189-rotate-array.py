class Solution(object):
    def rotate(self, arr, k):
        n = len(arr)
        k = (k)%(n)
        temp = []
        for i in range(n-k,n):
            temp.append(arr[i])
        for i in range(n-1,k-1,-1):
            arr[i]=arr[i-k]
        for i in range(k):
            arr[i] = temp[i]