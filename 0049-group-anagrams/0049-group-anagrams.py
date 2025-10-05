class Solution(object):
    def groupAnagrams(self, strs):
        n = len(strs)
        hashmap = {}
        for i in range(n):
            temp = [0]*26
            for c in strs[i]:
                temp[ord(c)-ord('a')]+= 1
            key = tuple(temp)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(strs[i])
        return sorted(list(hashmap.values()))

        