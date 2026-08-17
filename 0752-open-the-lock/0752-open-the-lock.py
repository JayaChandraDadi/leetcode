
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        if target in deadends:
            return -1
        if '0000' in deadends:
            return -1
        self.ans = float('inf')
        next_slot = {
            '0':'1',
            '1':'2',
            '2':'3',
            '3':'4',
            '4':'5',
            '5':'6',
            '6':'7',
            '7':'8',
            '8':'9',
            '9':'0'
        }
        previous_slot = {
            '0':'9',
            '1':'0',
            '2':'1',
            '3':'2',
            '4':'3',
            '5':'4',
            '6':'5',
            '7':'6',
            '8':'7',
            '9':'8'
        }
        q = deque()
        turns = 0
        q.append(('0000'))
        while(q):
            n = len(q)
            for i in range(n):
                s = q.popleft()
                if s==target:
                    return turns
                for pos in range(4):
                    next_string = s[:pos] + next_slot[s[pos]] + s[pos+1:]
                    previous_string = s[:pos] + previous_slot[s[pos]] + s[pos+1:]
                    if next_string not in visited and next_string not in deadends:
                        q.append((next_string))
                        visited.add((next_string))
                    if previous_string not in visited and previous_string not in deadends:
                        q.append((previous_string))
                        visited.add((previous_string))
            turns+=1
        return turns if s==target else -1