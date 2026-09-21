class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        myDict = {}

        for i in nums:
            if i in myDict:
                return True
            myDict[i] = myDict.get(i, 0) + 1
        return False
            
            


        
            
            