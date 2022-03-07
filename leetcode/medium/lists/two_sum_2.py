def twoSumTwo(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    res = []
    while left <= right:
        if numbers[left] + numbers[right] == target:
            res.append(left + 1)
            res.append(right + 1)
            return res
        elif numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1


ns = [2, 7, 11, 15]
t = 9

print(twoSumTwo(ns, t))
