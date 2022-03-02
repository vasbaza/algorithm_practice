def searchInsert(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] <= target:
            start = mid + 1
        if nums[mid] >= target:
            end = mid - 1
    return start


n = [1, 3, 5, 6]
t = 2

print(searchInsert(nums=n, target=t))
