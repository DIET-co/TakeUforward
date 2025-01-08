class Solution:
    # Function to print pattern17
    def pattern17(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            # Printing spaces before characters.
            for j in range(n - i - 1):
                print(" ", end="")
            
            # Printing characters.
            ch = 'A'
            breakpoint = (2 * i + 1) // 2
            for j in range(1, 2 * i + 2):
                print(ch, end="")
                if j <= breakpoint:
                    ch = chr(ord(ch) + 1)
                else:
                    ch = chr(ord(ch) - 1)
            
            # Printing spaces after characters.
            for j in range(n - i - 1):
                print(" ", end="")
            
            # Move to the next line for the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    #Create an instance of Solution class
    sol = Solution()
    
    sol.pattern17(N)
