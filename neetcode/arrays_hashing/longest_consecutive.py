class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for _, num in enumerate(nums):
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest
    

solution = Solution()

assert solution.longestConsecutive(nums = [100,4,200,1,3,2]) == 4
assert solution.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]) == 9