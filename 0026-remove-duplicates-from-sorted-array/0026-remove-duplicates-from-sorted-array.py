class Solution(object):
    def removeDuplicates(self, arr):
        i = 0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                continue
            else:
                arr[i+1] = arr[j]
                i+=1
        return i+1
            



        