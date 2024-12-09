from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr


sol = Solution()
print(sol.removeElement([3,2,2,3], 3))