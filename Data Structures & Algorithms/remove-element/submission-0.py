class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0

        for num in nums:
            if num != val:
                nums[p] = num
                p += 1

        return p