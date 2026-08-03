class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hashmap = {}
        for i in range(n):
            if hand[i] not in hashmap:
                hashmap[hand[i]] = 0
            hashmap[hand[i]]+=1
        hand.sort()
        for i in range(n):
            if hashmap[hand[i]]==0:
                continue
            for j in range(groupSize):
                curr = j + hand[i]
                if curr not in hashmap or hashmap[curr]==0:
                    return False
                hashmap[curr]-=1
        return True