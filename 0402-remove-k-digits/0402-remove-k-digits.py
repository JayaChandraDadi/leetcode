class Solution(object):
    def removeKdigits(self, num, k):
        n = len(num)
        st = []
        if k==n:
            return '0'
        for i in range(n):
            while st and int(st[-1])>int(num[i]) and k!=0:
                st.pop()
                k-=1
            st.append(num[i])
        while(k!=0):
            st.pop()
            k-=1
        output = ''.join(st)
        return str(int(output))