class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in range(len(asteroids)):
            flag = True
            while flag and st and st[-1]>0 and asteroids[i]<0:
                if st[-1]<abs(asteroids[i]):
                    st.pop()
                elif st[-1]==abs(asteroids[i]):
                    st.pop()
                    flag = False
                else:
                    flag = False
            if flag:
                st.append(asteroids[i])
        return st