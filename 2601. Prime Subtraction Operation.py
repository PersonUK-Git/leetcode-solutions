from math import sqrt
class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        def is_prime(n):
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True
        prev = 0
        
        for n in nums:
            upper_bound = n - prev
            largest_prime = 0
            for i in reversed(range(2, upper_bound)):
                if is_prime(i):
                    largest_prime = i
                    break

            if n - largest_prime <= prev:
                return False
            prev = n - largest_prime

        return True
sol = Solution()

print(sol.primeSubOperation([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]))
print(sol.primeSubOperation([4,9,6,10]))