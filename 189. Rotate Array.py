from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #OPTIMAL SOLUTION
        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k = k % len(nums)
        helper(0, len(nums)-1)
        helper(0, k-1)
        helper(k, len(nums)-1)

        # EASY SOLUTION
        # res = []
        # n = len(nums)
        # k = k % n
        # for i in range(n):
        #     res.append(nums[(n-k+i)%n])
        # return res

sol = Solution()

print(sol.rotate([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]