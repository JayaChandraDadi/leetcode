class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        maxlen = 0
        l = 0
        r = 0
        hashmap = {}
        while(r<n):
            if fruits[r] not in hashmap:
                hashmap[fruits[r]] = 0
            hashmap[fruits[r]]+=1
            if len(hashmap)<=2:
                maxlen = max(maxlen,r-l+1)
            else:
                while(len(hashmap)>2):
                    hashmap[fruits[l]]-=1
                    if hashmap[fruits[l]]==0:
                        hashmap.pop(fruits[l])
                    l+=1
            r+=1
        return maxlen

