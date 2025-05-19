class Solution(object):
    def minWindow(self, s, t):
        need = [0] * 256
        window = [0] * 256

        for c in t:
            need[ord(c)] += 1

        required = sum(1 for x in need if x > 0)
        formed = 0
        l = 0
        r = 0
        min_len = float('inf')
        start = 0

        while r < len(s):
            char_r = ord(s[r])
            window[char_r] += 1

            if need[char_r] > 0 and window[char_r] == need[char_r]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                char_l = ord(s[l])
                window[char_l] -= 1
                if need[char_l] > 0 and window[char_l] < need[char_l]:
                    formed -= 1
                l += 1

            r += 1

        return "" if min_len == float('inf') else s[start:start + min_len]