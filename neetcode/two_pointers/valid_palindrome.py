class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = list(filter(lambda x: (x.isalnum()), s))
        left = 0
        right = max(len(filtered_s) - 1, 0)
        while left < right:
            if filtered_s[left].lower() == filtered_s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True 
    
    def isPalindromeOptimized(self, s: str) -> bool:
        left, right = 0, len(s) -1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if  s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True 
        
solution = Solution()

# assert solution.isPalindrome(s = " ") == True
# assert solution.isPalindrome(s = "A man, a plan, a canal: Panama") == True
# assert solution.isPalindrome(s = "race a car") == False
# assert solution.isPalindrome(s = "raceq a car") == False
# assert solution.isPalindrome(s = "aa") == True
# assert solution.isPalindrome(s = "0P") == False

assert solution.isPalindromeOptimized(s = " ") == True
assert solution.isPalindromeOptimized(s = "A man, a plan, a canal: Panama") == True
assert solution.isPalindromeOptimized(s = "race a car") == False
assert solution.isPalindromeOptimized(s = "raceq a car") == False
assert solution.isPalindromeOptimized(s = "aa") == True
assert solution.isPalindromeOptimized(s = "0P") == False