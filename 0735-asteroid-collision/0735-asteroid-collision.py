class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        n = len(asteroids)
        st = []
        for i in range(n):
            if st and st[-1]>0 and asteroids[i]<0:
                while st and st[-1]>=0 and st[-1]<abs(asteroids[i]):
                    st.pop()
                if st and st[-1]>abs(asteroids[i]):
                    continue
                elif st and st[-1]==abs(asteroids[i]):
                    st.pop()
                    continue
                st.append(asteroids[i])
            else:
                st.append(asteroids[i])
        return st