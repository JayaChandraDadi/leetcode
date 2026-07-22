class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for i in range(len(operations)):
            ch = operations[i]
            if ch=='+':
                st.append(st[-1] + st[-2])
            elif ch=='D':
                st.append(2*st[-1])
            elif ch=='C':
                st.pop()
            else:
                st.append(int(ch))
        return sum(st)