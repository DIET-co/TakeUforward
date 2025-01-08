class Solution:
    # Function to print pattern18
    def pattern18(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            """ Inner loop for printing alphabets
            from 'A' + n - 1 - i to 'A' + n - 1."""
            for ch in range(ord('A') + n - 1 - i, ord('A') + n):
                print(chr(ch), end=" ")
            
            # Move to the next line for the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern18(N)
