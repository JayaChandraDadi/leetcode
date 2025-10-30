class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0 
        temp = []
        while(i<m and j<n):
            if nums1[i]<=nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        while(i<m):
            temp.append(nums1[i])
            i+=1
        while(j<n):
            temp.append(nums2[j])
            j+=1
        for i in range(len(temp)):
            nums1[i] = temp[i]
               