class Solution(object):
    def isPalindrome(self, s):
        i = 0
        string = ''.join(c for c in s if c.isalnum()).lower()
        j = len(string)-1
        while(i<=j):
            if string[i]!=string[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        