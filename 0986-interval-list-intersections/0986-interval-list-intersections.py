class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        i = 0
        j = 0
        ans = []
        while(i<n1 and j<n2):
            first_0 = firstList[i][0]
            second_0 = secondList[j][0]
            first_1 = firstList[i][1]
            second_1 = secondList[j][1]
            if first_0<=second_0 and second_0<=first_1:
                ans.append([second_0,min(first_1,second_1)])
                if first_1<=second_1:
                    i+=1
                else:
                    j+=1
            elif first_0>=second_0 and first_0<=second_1:
                ans.append([first_0,min(first_1,second_1)])
                if first_1<=second_1:
                    i+=1
                else:
                    j+=1
            else:
                if first_1<second_0:
                    i+=1
                else:
                    j+=1
       
        return ans