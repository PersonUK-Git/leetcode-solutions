from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #optimal solution
        res, count = 0,0
        for i in nums:
            if count == 0:
                res = i
            count += (1 if i == res else -1)
        return res
    
        #not so optimal (HASH MAP WAY)

        # count = {}
        # res, maxCount = 0, 0
        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n], maxCount)
        # return res

sol =  Solution()

print(sol.majorityElement([3,2,3])) # 3