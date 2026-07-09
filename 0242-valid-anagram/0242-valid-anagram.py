class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = [0]*(26)
        t_map = [0]*(26)
        if len(t)!=len(s):
            return False
        for i in range(len(t)):
            s_map[ord(s[i]) - ord('a')]+=1
            t_map[ord(t[i]) - ord('a')]+=1
        for i in range(26):
            if s_map[i]!=t_map[i]:
                return False
        return True