class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}

        for word in strs:
            key = "".join(sorted(word))
            myDict[key] = myDict.get(key, []) + [word]

        return list(myDict.values())
            




            