def sortedSquares(nums: list[int]) -> list[int]:
    squared = [num ** 2 for num in nums]
    left_pointer = 0
    right_pointer = len(squared) - 1
    res = []

    while left_pointer <= right_pointer:
        if squared[left_pointer] < squared[right_pointer]:
            res.append(squared[right_pointer])
            right_pointer -= 1
        else:
            res.append(squared[left_pointer])
            left_pointer += 1
    res.reverse()
    return res


n = [-7, -3, 2, 3, 11]


print(sortedSquares(n))
