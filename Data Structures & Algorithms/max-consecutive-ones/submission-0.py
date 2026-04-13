class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_max = 0
        consecutive_counter = 0
        
        for num in nums:
            if num == 1:
                consecutive_counter += 1
                if consecutive_counter > consecutive_max:
                    consecutive_max = consecutive_counter
            else:
                consecutive_counter = 0

        return consecutive_max