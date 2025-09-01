class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for word in strs:
            temp = [0]*26
            for c in word:
                temp[ord(c)-ord('a')]+=1
            res[tuple(temp)].append(word)
        return list(res.values())