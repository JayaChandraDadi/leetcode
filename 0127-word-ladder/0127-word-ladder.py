from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        wordlist = set(wordList)
        q.append((beginWord,0))
        word_length = len(beginWord)
        steps = 0
        while(q):
            word,steps = q.popleft()
            if word==endWord:
                return steps+1
            for position in range(word_length):
                for i in range(26):
                    ch = chr(ord('a') + i)
                    new_word = word[:position] + ch + word[position+1:]
                    if new_word in wordlist:
                        q.append((new_word,steps+1))
                        wordlist.remove(new_word)
        return 0