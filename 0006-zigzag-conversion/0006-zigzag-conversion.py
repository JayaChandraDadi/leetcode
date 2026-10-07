class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows>=len(s) or numRows==1:
            return s
        mat = ['']*numRows
        curr_row = 0
        direction = 0
        i = 0
        while(i<len(s)):
            if direction==0:
                while(i<len(s) and curr_row<numRows):
                    mat[curr_row]+=s[i]
                    i+=1
                    curr_row+=1
                curr_row-=2
                direction = 1
            else:
                while(i<len(s) and curr_row>0):
                    mat[curr_row]+=s[i]
                    i+=1
                    curr_row-=1
                direction = 0
        return "".join(mat)