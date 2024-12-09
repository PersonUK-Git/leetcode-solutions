class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""             # To hold the compressed result
        cnt, n = 1, len(word)  # Initialize count to 1, n to length of input string
        ch = word[0]           # Start with the first character in the word
        
        for i in range(1, n):  # Loop from the second character to the end of the string
            if word[i] == ch and cnt < 9:
                cnt += 1       # Increment count if the current character matches 'ch' and count is less than 9
            else:
                # Add the count and character to the compressed result
                comp += str(cnt) + ch
                ch = word[i]   # Update 'ch' to the new character
                cnt = 1        # Reset count to 1 for the new character group
        
        # Add the final count and character to the compressed result
        comp += str(cnt) + ch
        return comp

    
sol = Solution()
print(sol.compressedString("aaabcccd"))
print(sol.compressedString("abcde"))
print(sol.compressedString("aabbddbebebdebded"))