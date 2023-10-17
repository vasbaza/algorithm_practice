class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for key, value in counts.items():
            freq[value].append(key)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
