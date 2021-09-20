# ToDo: уменьшить сложность с O(n**2)

def twoSum(nums, target):
    for i, value in enumerate(nums):
        for j, value in enumerate(nums):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum(nums = [3, 3], target = 6))


