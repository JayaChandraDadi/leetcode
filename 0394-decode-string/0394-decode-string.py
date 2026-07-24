class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        n = len(s)
        res = ''
        i = 0
        while(i<n):
            if s[i]=='[':
                st.append(s[i])
                i+=1
            elif s[i].isdigit():
                num = 0
                while(s[i].isdigit()):
                    num = num*10 + int(s[i])
                    i+=1
                st.append(num)
            elif s[i].isalpha():
                word = ''
                while(i<n and s[i].isalpha()):
                    word+=s[i]
                    i+=1
                st.append(word)
            else:
                temp = ''
                while(st[-1]!='['):
                    ch = st.pop()
                    temp = ch + temp
                st.pop()
                times = int(st.pop())
                st.append(times*temp)
                i+=1
        return ''.join(st)