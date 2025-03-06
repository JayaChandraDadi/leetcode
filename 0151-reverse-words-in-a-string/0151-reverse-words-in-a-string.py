class Solution(object):
    def reverseWords(self, s):
        ct = 0
        ans = []
        for i in s:
            if i==' ':
                ct+=1
            if ct>1:
                continue
            else:
                ct = 0
                ans.append(i)
        return " ".join("".join(ans).split()[::-1])
        
        