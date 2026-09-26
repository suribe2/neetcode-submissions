class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        maxRes = 0

        while l < r:
            length = r - l 
            area = min(heights[l], heights[r]) * length
            

            if heights[l] < heights[r]:
                l += 1
                res = area
            else:
                r -= 1
                res = area


            if area > maxRes:
                maxRes = res

        return maxRes
                


