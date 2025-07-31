class Solution(object):
    def minInsertions(self, s):
        n1 = len(s)
        n2 = n1
        s1 = s
        s2 = s[::-1]
        prev = [0]*(n2+1) 
        for i in range(1,n1+1):
            temp = [0]*(n2+1)
            for j in range(1,n2+1):
                if s1[i-1]==s2[j-1]:
                    temp[j] = 1+prev[j-1]
                else:
                    temp[j] = max(prev[j],temp[j-1])
            prev = temp
        return n1-prev[n2]