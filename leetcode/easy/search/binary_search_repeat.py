from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]


s = Solution()
# result1 = s.firstBadVersion(versions1)
# print(result1)
# print(result1 == bad1)

# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# # target2 = 1
# ex = [5, 6, 7, 1, 2, 3, 4]

# nums = [-1, -100, 3, 99]
# k = 2
# # target2 = 1
# ex = [3, 99, -1, -100]

# nums = [1, 2]
# k = 3
# # target2 = 1
# ex = [2, 1]

nums = [1, 2, 3]
k = 4
# target2 = 1
ex = [3, 1, 2]
# #
s.rotate(nums, k)
print(nums == ex)
#
# nums3 = [1, 2, 3, 4, 5]
# target3 = 6
# result3 = s.search(nums3, target3)
# print(result3 == -1)
#
# nums4 = [-1, 0, 2, 9, 13, 15]
# target4 = 9
# result4 = s.search(nums4, target4)
# print(result4 == 3)
