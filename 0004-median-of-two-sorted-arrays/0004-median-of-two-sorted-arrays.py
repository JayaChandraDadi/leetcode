class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        n1 = len(nums1)
        n2 = len(nums2)
        low = 0
        left = (n1+n2+1)//2
        high = n1
        n = n1+n2
        while(low<=high):
            mid1 = (low+high)//2
            mid2 = left-mid1
            r1 = nums1[mid1] if mid1<n1 else float("inf")
            r2 = nums2[mid2] if mid2<n2 else float("inf")
            l1 = nums1[mid1-1] if mid1-1>=0 else float("-inf")
            l2 = nums2[mid2-1] if mid2-1>=0 else float("-inf")
            if l1<=r2 and l2<=r1:
                if n%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            elif l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return -1

            



        