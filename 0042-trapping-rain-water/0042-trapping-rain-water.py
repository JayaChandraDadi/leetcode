class Solution(object):
    def trap(self, height):
        total = 0
        prefixmax = [-1]*len(height)
        prefixmax[0] = height[0]
        for i in range(1,len(height)-1):
            prefixmax[i] = max(prefixmax[i-1],height[i])
        suffixmax = [-1]*len(height)
        suffixmax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            suffixmax[i] = max(suffixmax[i+1],height[i])
        for i in range(len(height)):
            leftmax = prefixmax[i]
            rightmax = suffixmax[i]
            if height[i]<leftmax and height[i]<rightmax:
                total+=min(leftmax,rightmax)-height[i]
        return total


        