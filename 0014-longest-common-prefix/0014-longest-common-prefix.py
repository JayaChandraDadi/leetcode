class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            n1 = len(prefix)
            n2 = len(strs[i])
            temp = strs[i]
            j = 0
            k = 0
            while(j<n1 and k<n2):
                if prefix[j]!=temp[k]:
                    break
                j+=1
                k+=1
            prefix = prefix[:j]
            if prefix=='':
                return ''
        return prefix