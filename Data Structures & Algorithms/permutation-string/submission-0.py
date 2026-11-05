class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        
        #count letters in s1
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i : i + len(s1)]
        
            count2 = {}
            for char in window:
                count2[char] = count2.get(char, 0) + 1

                if count1 == count2:
                    return True

        return False
        
        