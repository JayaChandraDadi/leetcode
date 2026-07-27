import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        low = 0
        high = len(nums) - 1

        while low <= high:
            pivot = nums[random.randint(low, high)]

            left = low
            current = low
            right = high

            while current <= right:
                if nums[current] < pivot:
                    nums[left], nums[current] = nums[current], nums[left]
                    left += 1
                    current += 1

                elif nums[current] > pivot:
                    nums[current], nums[right] = nums[right], nums[current]
                    right -= 1

                else:
                    current += 1

            # [low ... left-1] contains values < pivot
            # [left ... right] contains values == pivot
            # [right+1 ... high] contains values > pivot

            if target < left:
                high = left - 1
            elif target > right:
                low = right + 1
            else:
                return nums[target]