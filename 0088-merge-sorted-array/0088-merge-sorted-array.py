class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = 0
        while(i>-1 and j<n):
            if nums1[i]>nums2[j]:
                nums1[i],nums2[j] = nums2[j],nums1[i]
                i-=1
                j+=1
            else:
                break
        for i in range(m,n+m):
            nums1[i] = nums2[i-m]
        nums1.sort()
        
        
            