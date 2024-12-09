from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Use a set for O(1) lookup
        seen = set()
        
        for num in arr:
            # Check if double of current number exists
            if num * 2 in seen:
                return True
            
            # Check if half of current number exists (for even numbers)
            if num % 2 == 0 and num // 2 in seen:
                return True
            
            # Add current number to set
            seen.add(num)
        
        return False