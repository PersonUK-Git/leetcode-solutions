class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        new_arr = []
        for i in range(len(s)):
            new_arr.append(s[i])
            print(new_arr)
        for i in range(len(s)):
            new_arr.append(s[i])
            print(new_arr)
        goal = [goal[i] for i in range(len(goal))]
        print(goal)
        for i in range(len(s)):  # We only need to check up to `len(s)` for a rotation
            if new_arr[i:i + len(s)] == goal:
                return True
        
        return False


sol = Solution()

print(sol.rotateString("abcde", "cdeab"))