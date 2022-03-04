def moveZeroes(nums: list[int]) -> None:
    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer <= right_pointer:
        if nums[left_pointer] == 0:
            nums.append(nums[left_pointer])
            nums.remove(nums[left_pointer])
            left_pointer += 1
        else:
            left_pointer += 1


def moveZeroesFast(nums: list[int]) -> None:
    start = 0
    for i, _ in enumerate(nums):
        if nums[i] != 0:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1


n = [0]
# n = [0, 1, 0, 3, 12]
# n = [0, 1, 0, 3, 1, 1, 0, 0, 23, 0, 1, 5, 0, 12, 0]
# n = [0, 0, 1]
# n = [1, 1, 0, 3, 1, 1, 0, 0, 23, 0, 1, 5, 0, 12, 0]

moveZeroesFast(n)

print(n)
