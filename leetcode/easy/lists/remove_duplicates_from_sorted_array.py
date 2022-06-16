from typing import List


def remove_duplicates(nums: List[int]) -> int:
    current_index = 0
    next_index = 1

    while next_index <= len(nums) - 1:
        while nums[current_index] == nums[next_index]:
            del nums[next_index]
            nums.append(-200)

        if nums[next_index] == -200:
            break
        current_index += 1
        next_index += 1

    return next_index


assert remove_duplicates([1, 1, 2]) == 2, "Fail"
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5, "Fail"
assert remove_duplicates([1, 1]) == 1, "Fail"
