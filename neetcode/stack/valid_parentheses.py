class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        stack = []
        bracets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for bracet in s_list:
            if bracet in bracets and stack:
                if stack[-1] == bracets[bracet]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracet)
        return len(stack) == 0
    
solution = Solution()

assert solution.isValid(s = "()") == True
assert solution.isValid(s = "()[]{}") == True
assert solution.isValid(s = "(]") == False
assert solution.isValid(s = "((()))") == True
assert solution.isValid(s = "((([])))") == True
assert solution.isValid(s = "(){}}{") == False

