class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        time = []
        n = len(position)
        for i in range(n):
            time.append((target-position[i])/speed[i])
        cars = [(position[i],time[i]) for i in range(n)]
        cars.sort(key=lambda x: x[0], reverse=True)
        maxtime = float('-inf')
        fleet = 0
        for pos,time in cars:
            if maxtime<time:
                fleet+=1
                maxtime = time
        return fleet