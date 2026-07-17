class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        i = 0
        st = []
        while(i<n):
            while(i<n and path[i]=='/'):
                i+=1
            j = i
            if i == n:
                break
            while(i<n and path[i]!='/'):
                i+=1
            temp = path[j:i]
            if temp=='.':
                continue
            elif temp=='..' and len(st)!=0:
                st.pop()
            elif temp=='..' and len(st)==0:
                continue
            else:
                st.append(temp)
        res = '/'
        for i in range(len(st)):
            word = st[i]
            res+=word
            if i!=len(st)-1:
                res+='/'
        return res
