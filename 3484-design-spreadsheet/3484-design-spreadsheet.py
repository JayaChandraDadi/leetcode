class Spreadsheet:

    def __init__(self, rows: int):
        self.hashmap = {}
    def setCell(self, cell: str, value: int) -> None:
        self.hashmap[cell] = value


    def resetCell(self, cell: str) -> None:
        if cell not in self.hashmap:
            return
        self.hashmap[cell] = 0
    def getValue(self, formula: str) -> int:
        i = 1
        s1 = ''
        while(formula[i]!='+' and i<len(formula)):
            s1+=formula[i]
            i+=1
        s2 = formula[i+1:len(formula)]
        num1 = 0
        num2 = 0
        if s1.isdigit():
            num1 = int(s1)
        else:
            if s1 in self.hashmap:
                num1 = self.hashmap[s1]
        if s2.isdigit():
            num2 = int(s2)
        else:
            if s2 in self.hashmap:
                num2 = self.hashmap[s2]
        return num1 + num2
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)