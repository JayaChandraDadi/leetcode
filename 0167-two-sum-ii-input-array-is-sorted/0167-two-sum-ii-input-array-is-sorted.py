class Solution(object):
    def twoSum(self, numbers, target):
       hashmap = {}
       for i in range(len(numbers)):
        sum1 = numbers[i]
        rem = target-sum1
        if rem in hashmap:
            return [hashmap[rem]+1,i+1]
        hashmap[sum1] = i
       