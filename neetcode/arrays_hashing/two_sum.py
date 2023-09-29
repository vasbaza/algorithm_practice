class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            second_num = target - num
            isKeyAlreadyAdded = False if prevMap.get(second_num, -1) == -1 else True
            if not isKeyAlreadyAdded:
                prevMap[num] = i
            else:
                return [i, prevMap[second_num]]
            

solution = Solution()

# assert solution.twoSum(nums = [2,7,11,15], target = 9) == [0, 1] or solution.twoSum(nums = [2,7,11,15], target = 9) == [1, 0]
print(solution.twoSum(nums = [2,7,11,15], target = 9))
print(solution.twoSum(nums = [3,2,4], target = 6))
print(solution.twoSum(nums = [3, 3], target = 6))
# assert (solution.twoSum(nums = [3,2,4], target = 6) == [1, 2] or solution.twoSum(nums = [2,7,11,15], target = 9) == [2, 1])
# assert solution.twoSum(nums = [3, 3], target = 6) == [0, 1] or solution.twoSum(nums = [2,7,11,15], target = 9) == [1, 0]
        
