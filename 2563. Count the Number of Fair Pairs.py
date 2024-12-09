class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def bin_search(l, r, target):
            while l <= r:
                m = (l + r) //2
                if nums[m] >= target:
                    r = m -1
                else:
                    l = m + 1
            return r
        nums.sort()
        res = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            high = upper - nums[i]

            res += ( bin_search(i +1, len(nums) - 1, high + 1) -
                     bin_search(i +1, len(nums) - 1, low))

        return res

sol = Solution()

print(sol.countFairPairs([1,2,3,4,5], 2, 4))
print(sol.countFairPairs([0,1,7,4,4,5], 3, 6))