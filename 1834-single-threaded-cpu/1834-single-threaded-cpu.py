import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda x:x[0])
        pq = []
        current_time = tasks[0][0]
        i = 0
        while(i<n and current_time>=tasks[i][0]):
            _,processing,index = tasks[i]
            heapq.heappush(pq,(processing,index))
            i+=1
        ans = []
        while(pq or i<n):
            if pq:
                time,index = heapq.heappop(pq)
                ans.append(index)
                current_time+=time
                while(i<n and current_time>=tasks[i][0]):
                    _,processing,index = tasks[i]
                    heapq.heappush(pq,(processing,index))
                    i+=1
            else:
                current_time = tasks[i][0]
                while(i<n and current_time>=tasks[i][0]):
                    _,processing,index = tasks[i]
                    heapq.heappush(pq,(processing,index))
                    i+=1
        return ans