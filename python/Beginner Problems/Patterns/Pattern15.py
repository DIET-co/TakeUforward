class Solution:
    # Function to print pattern15
    def pattern15(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            """Inner loop will loop for i times and
            print alphabets from A to A + (n - i - 1)."""
            for ch in range(ord('A'), ord('A') + n - i):
                print(chr(ch), end="")
                
            """As soon as the letters for each iteration
            are printed, we move to the next row and give
            a line break otherwise all letters would get
            printed in 1 line."""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern15(N)
