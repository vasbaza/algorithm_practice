class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1): 
            output[i] *= postfix
            postfix *= nums[i]

        return output

solution = Solution()

assert solution.productExceptSelf(nums = [1,2,3,4])== [24,12,8,6]
assert solution.productExceptSelf(nums = [-1,1,0,-3,3])== [0,0,9,0,0]
