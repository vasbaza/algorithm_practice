class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) -1
        while l < r:
            current_sum = numbers[r] + numbers[l]
            if current_sum == target:
                return [l+1, r+1]
            else:
                if current_sum > target:
                    r -= 1
                else:
                    l += 1
        return [l+1, r+1]


solution = Solution()

assert solution.twoSum(numbers = [2, 7, 11, 15], target = 9) == [1, 2]
assert solution.twoSum(numbers = [1, 3, 4, 5, 7, 11], target = 9) == [3, 4]
assert solution.twoSum(numbers = [2,3,4], target = 6) == [1, 3]
assert solution.twoSum(numbers = [-1, 0], target = -1) == [1, 2]