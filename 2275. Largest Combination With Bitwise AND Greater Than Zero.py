class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(1 for candidate in candidates if candidate & (1 << i))
            ans = max(ans, cnt)
        return ans
    
sol = Solution()

print(sol.largestCombination([16,17,71,62,12,24,14]))
print(sol.largestCombination([8,8]))
print(sol.largestCombination([3,1,3,1,3,1,3,1]))
# write a print function
