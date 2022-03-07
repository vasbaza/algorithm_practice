def rotate(nums: list[int], k: int) -> None:
    """
        Given an array, rotate the array to the right by k steps, where k is non-negative.

        Example:

        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

     """
    for i in range(k):
        nums.insert(0, nums[- 1])
        nums.pop(- 1)


ns = [-1, -100, 3, 99]
ks = 2

rotate(ns, ks)

print(ns)
