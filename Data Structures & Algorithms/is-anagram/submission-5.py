class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        myDict1 = {}
        myDict2 = {}

        for char in s:
            myDict1[char] = myDict1.get(char, 0) + 1
        
        for char in t:
            myDict2[char] = myDict2.get(char, 0) + 1

        return myDict1 == myDict2


            