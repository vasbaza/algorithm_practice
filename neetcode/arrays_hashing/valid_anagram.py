class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False
        return True

    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)
    
solution = Solution()

assert solution.isAnagram(s = "anagram", t = "nagaram") == True
assert solution.isAnagram(s = "rat", t = "car") == False
assert solution.isAnagram(s = "a", t = "b") == False
assert solution.isAnagram(s = "a", t = "a") == True
assert solution.isAnagram(s = "a", t = "aa") == False