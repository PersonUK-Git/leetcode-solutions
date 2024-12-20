class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1
       
        while l < r:
            area = (r - l) * min(height[l], height[r])
           
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))