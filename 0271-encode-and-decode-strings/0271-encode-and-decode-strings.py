class Codec:
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for word in strs:
            ans+=str(len(word)) + '#' + word
        return ans
    def decode(self, s: str) -> List[str]:
        n = len(s)
        j = 0
        ans = []
        i = 0
        while(i<len(s)):
            j = i
            while(s[j]!='#'):
                j+=1
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j+1+length
        return ans
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))