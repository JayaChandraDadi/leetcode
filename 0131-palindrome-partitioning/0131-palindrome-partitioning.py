class Solution(object):
    def ispalindrome(self,s,left,right):
        while(left<right):
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def partation(self,s,path,ans,index):
        if index==len(s):
            ans.append(list(path))
            return 
        for i in range(index,len(s)):
            if self.ispalindrome(s,index,i):
                path.append(s[index:i+1])
                self.partation(s,path,ans,i+1)
                path.pop()
        return ans
    def partition(self, s):
        return self.partation(s,[],[],0)