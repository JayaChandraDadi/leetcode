from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        queue = deque()
        queue.append([beginWord,1])
        while(len(queue)!=0):
            word,length = queue.popleft()
            if word==endWord:
                return length
            for i in range(len(word)):
                for ch in range(ord('a'),ord('z')+1):
                    newword = word[:i]+chr(ch)+word[i+1:]
                    if newword in wordset:
                        wordset.remove(newword)
                        queue.append([newword,length+1])
        return 0        