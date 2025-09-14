class Solution(object):
    def carFleet(self, target, position, speed):
        st = []
        n = len(position)
        matrix = []
        for i in range(n):
            matrix.append([position[i],speed[i]])
        matrix.sort(key=lambda x: x[0], reverse=True)
        for p,s in matrix:
            time = float((target-p))/s
            st.append(time)
            if len(st)>1 and st[-1]<=st[-2]:
                st.pop()
        return len(st)