class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))

        sP = 0
        tP = 0

        while sP < len(s) and tP < len(t):
            if sortedS[sP] == sortedT[tP]:
                sP +=1
                tP +=1
            else:
                return False
        return True



            