class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in indexes:
                return [indexes[difference], i]
            else:
                indexes[nums[i]] = i