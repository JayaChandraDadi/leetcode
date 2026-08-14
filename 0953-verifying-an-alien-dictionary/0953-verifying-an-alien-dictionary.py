class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        order = list(order)
        for i in range(len(order)):
            hashmap[order[i]] = i
        for i in range(1,len(words)):
            word1 = words[i-1]
            word2 = words[i]
            found = False
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    found = True
                    if hashmap[word1[j]]>hashmap[word2[j]]:
                        return False
                    break
            if found==False and len(word1)>len(word2):
                return False
        return True