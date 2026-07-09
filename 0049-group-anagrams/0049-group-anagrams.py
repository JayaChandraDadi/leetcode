class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hashmap = {}
        for word in strs:
            temp = [0]*(26)
            for ch in word:
                temp[ord(ch) - ord('a')]+=1
            key = tuple(temp)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        ans = []
        for key,arr in hashmap.items():
            ans.append(arr)
        return ans