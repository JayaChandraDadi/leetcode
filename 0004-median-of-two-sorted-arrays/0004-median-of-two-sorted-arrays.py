class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)+len(nums2)
        ct = 0
        index1 = n//2
        index2 = n//2-1
        i = 0
        j = 0
        el1 = -1
        el2 = -1
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                if index1==ct:
                    el1 = nums1[i]
                if index2==ct:
                    el2 = nums1[i]
                ct+=1
                i+=1
            else:
                if index1==ct:
                    el1 = nums2[j]
                if index2==ct:
                    el2 = nums2[j]
                ct+=1
                j+=1
        while(i<len(nums1)):
            if index1==ct:
                    el1 = nums1[i]
            if index2==ct:
                    el2 = nums1[i]
            ct+=1
            i+=1
        while(j<len(nums2)):
            if index1==ct:
                    el1 = nums2[j]
            if index2==ct:
                    el2 = nums2[j]
            ct+=1
            j+=1
        if n%2==1:
            return el1
        else:
            return (el1+el2)/2.0




            
        