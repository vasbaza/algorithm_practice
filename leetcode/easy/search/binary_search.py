"""Binary search"""


def search(nums: list[int], target: int):
    current_index = int(len(nums) / 2)
    while nums[current_index] != target:
        if current_index + 1 > len(nums) - 1 or nums[current_index] < target < nums[current_index + 1]:
            return -1
        if target > nums[current_index]:
            current_index += int(len(nums[current_index:]) / 2)
        elif target < nums[current_index]:
            current_index -= int(len(nums[:current_index + 1]) / 2)
    return current_index


# print(binary_search([0, 1], 1))
print(search([-1, 0, 3, 5, 9, 12], 2))
