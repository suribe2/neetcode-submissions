class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myTable = {}
        myTable2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            myTable[char] = myTable.get(char, 0) + 1

        for char in t:
            myTable2[char] = myTable2.get(char, 0) + 1 

        if myTable == myTable2:
            return True
        else:
            return False
            

            