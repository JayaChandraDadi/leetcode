class Solution(object):
    def minDistance(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        prev = [0]*(n2+1) 
        for i in range(1,n1+1):
            temp = [0]*(n2+1)
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    temp[j] = 1+prev[j-1]
                else:
                    temp[j] = max(prev[j],temp[j-1])
            prev = temp
        return (n1-prev[n2])+(n2-prev[n2])
        