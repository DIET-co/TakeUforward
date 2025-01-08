class Solution:
    # Function to print pattern16
    def pattern16(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            # Defining character for each row.
            ch = chr(ord('A') + i)
            for j in range(i + 1):
                
                """same char is to be printed
                i times in that row."""
                print(ch, end="")
                
            """ As soon as the letters for each 
            iteration are printed, we move to the
            next row and give a line break otherwise
            all letters would get printed in 1 line. """
            print()

N = 5

# Create an instance of Solution class
sol = Solution()

sol.pattern16(N)
