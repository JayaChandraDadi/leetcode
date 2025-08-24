class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        j = 0
        n1 = len(haystack)
        n2 = len(needle)
        while(i<n1 and j<n2):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==n2:
                    return i-n2
            else:
                i = i-j+1 
                j = 0     
        return -1
        