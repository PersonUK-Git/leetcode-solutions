from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0

print(Solution().hIndex([3,0,6,1,5])) # 3