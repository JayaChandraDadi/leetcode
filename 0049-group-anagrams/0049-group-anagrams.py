class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        n = len(strs)
        ans = []
        for i in range(n):
            word_map = [0]*26
            for ch in strs[i]:
                word_map[ord(ch) - ord('a')]+=1
            word_map = tuple(word_map)
            if word_map not in hashmap:
                hashmap[word_map] = []
            hashmap[word_map].append(strs[i])
        for word_map,arr in hashmap.items():
            ans.append(arr)
        return ans
