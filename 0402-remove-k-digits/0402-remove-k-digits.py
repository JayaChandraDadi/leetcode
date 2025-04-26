class Solution(object):
    def removeKdigits(self, num, k):
        n = len(num)
        if k==n:
            return '0'
        st = []
        for i in range(n):
            while st and st[-1]>num[i] and k!=0:
                st.pop()
                k-=1
            st.append(num[i])
        while(k!=0):
            st.pop()
            k-=1
        output = ''.join(st)
        return str(int(output))

