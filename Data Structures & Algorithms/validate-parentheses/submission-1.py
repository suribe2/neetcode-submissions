class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack[-1] != closeToOpen[char]:
                    return False
                stack.pop()
        
        return not stack
            
            