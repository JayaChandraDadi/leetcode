class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n==0:
            return 0
        maxlen = 1
        curr_len = 1
        previous_direction = None
        i = 1
        while(i<n):
            if arr[i-1]>arr[i]:
                current_direction = 1
            elif arr[i-1]<arr[i]:
                current_direction = -1
            else:
                previous_direction = None
                i+=1
                curr_len = 1
                continue
            if current_direction!=previous_direction:
                curr_len+=1
                maxlen = max(maxlen,curr_len)
            else:
                curr_len = 1
                previous_direction = None
                continue
            previous_direction = current_direction
            i+=1
        return maxlen