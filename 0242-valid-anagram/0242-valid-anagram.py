class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        if len(t)!=len(s):
            return False
        for i in range(len(t)):
            if s[i] not in s_map:
                s_map[s[i]] = 0
            s_map[s[i]]+=1
            if t[i] not in t_map:
                t_map[t[i]] = 0
            t_map[t[i]]+=1
        for ch,freq in s_map.items():
            if ch not in t_map or freq!=t_map[ch]:
                return False
        return True