class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = 0
        while(i>=0 and j<n):
            if nums1[i]>=nums2[j]:
                nums1[i],nums2[j] = nums2[j],nums1[i]
                i-=1
                j+=1
            else:
                i-=1
                j+=1
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()