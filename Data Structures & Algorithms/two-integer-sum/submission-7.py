class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in indexes:
                return [indexes[difference], i]
            indexes[n] = i