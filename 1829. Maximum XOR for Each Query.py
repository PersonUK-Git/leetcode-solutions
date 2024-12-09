class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        n = len(nums)
        xorr = nums[0]
        max_xor = (1 << maximumBit) - 1
        #print(max_xor)
        for i in range(1, n):
            xorr ^= nums[i]
            #print(" inside for",xorr)
        
        ans = []
        for i in range(n):
            ans.append(xorr ^ max_xor)
            #print("answer" ,ans)
            xorr ^= nums[n - 1 - i]
            #print("xorr after ans",xorr)
        
        return ans
    
sol = Solution()
print(sol.getMaximumXor([3, 10, 5, 25, 2, 8], 2))
print(sol.getMaximumXor([0,1,1,3], 2))