class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
    

solution = Solution()

assert solution.containsDuplicate([0]) == False
assert solution.containsDuplicate([0, 0]) == True
assert solution.containsDuplicate([1,2,3,1]) == True
assert solution.containsDuplicate([1,2,3,4]) == False
assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True