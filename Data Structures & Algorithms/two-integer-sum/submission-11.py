class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in myDict:
                return [myDict[diff], i]
            else: 
                myDict[num] = i 

        
