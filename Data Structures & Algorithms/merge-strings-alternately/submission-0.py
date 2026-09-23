class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1, p2 = 0, 0

        newStr = ""

        while p1 < len(word1) and p2 < len(word2):
            newStr += word1[p1]
            p1 += 1
            newStr += word2[p2]
            p2 += 1

        if p1 < len(word1):
            newStr += word1[p1:]
        else:
            newStr += word2[p2:]

        return newStr


            



