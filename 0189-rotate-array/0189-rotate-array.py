class Solution(object):
    def rotate(self, arr, k):
        n  = len(arr)
        k = k%n 
        temp = []
        for i in range(n-k,n):
            temp.append(arr[i])
        for i in range(n-k-1,-1,-1):
            arr[i+k] = arr[i]
        for i in range(k):
            arr[i] = temp[i]