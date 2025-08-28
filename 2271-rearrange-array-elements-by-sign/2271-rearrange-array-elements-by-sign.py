class Solution(object):
    def rearrangeArray(self, nums):
       pos = []
       neg = []
       temp = []
       n = len(nums)
       for i in range(n):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
       i = 0
       j = 0
       while(i<len(pos) or j<len(neg)):
        if not temp or temp[-1]<0:
            temp.append(pos[i])
            i+=1
        else:
            temp.append(neg[j])
            j+=1
       return temp
