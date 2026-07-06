class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.hashmap = {}
        for word in dictionary:
            if len(word)<=2:
                if word not in self.hashmap:
                    self.hashmap[word] = []
                self.hashmap[word] = word
                continue
            start = word[0]
            end = word[len(word)-1]
            ct = 0
            for i in range(1,len(word)-1):
                ct+=1
            abrevation = start + str(ct) + end
            if abrevation not in self.hashmap:
                self.hashmap[abrevation] = []
            self.hashmap[abrevation].append(word)
            
    def isUnique(self, word: str) -> bool:
        abrevation = ''
        start = word[0]
        end = word[len(word)-1]
        ct = 0
        for i in range(1,len(word)-1):
            ct+=1
        abrevation = start + str(ct) + end
        if abrevation in self.hashmap:
            for string in self.hashmap[abrevation]:
                if string!=word:
                    return False
        return True
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)