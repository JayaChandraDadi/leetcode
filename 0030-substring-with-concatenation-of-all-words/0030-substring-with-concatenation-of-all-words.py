class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        string_length = len(words)*(len(words[0]))
        word_len = len(words[0])
        if len(s)<string_length:
            return []
        word_map = {}
        for i in range(len(words)):
            if words[i] not in word_map:
                word_map[words[i]] = 0
            word_map[words[i]]+=1
        hashmap = {}
        i = 0
        ans = set()
        for start in range(word_len):
            i = start
            hashmap = {}
            while(i<start + string_length):
                word = s[i:i+word_len]
                if word not in hashmap:
                    hashmap[word] = 0
                hashmap[word]+=1
                i+=word_len
            l = start
            r = start + string_length
            while(r<len(s)):
                if hashmap==word_map:
                    ans.add(l)
                left_word = s[l:l+word_len]
                right_word = s[r:r+word_len]
                hashmap[left_word]-=1
                if hashmap[left_word]==0:
                    del hashmap[left_word]
                if right_word not in hashmap:
                    hashmap[right_word] = 0
                hashmap[right_word]+=1
                l+=word_len
                r+=word_len
            if hashmap==word_map:
                ans.add(l)
        return list(ans)