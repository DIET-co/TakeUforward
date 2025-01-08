class Solution:
    # Function to print pattern19
    def pattern19(self, n):
        # Print the upper half pattern
        
        # Store the initial spaces.
        iniS = 0
        
        for i in range(n):
            # Printing the stars in the row.
            print("*" * (n - i), end="")
            
            # Printing the spaces in the row.
            print(" " * iniS, end="")
            
            # Printing the stars in the row.
            print("*" * (n - i))
            
            """ The spaces increase by 2 
            every time we hit a new row."""
            iniS += 2
        
        # Print the lower half pattern
        
        # Store the initial spaces.
        iniS = 2 * n - 2
        
        for i in range(1, n + 1):
            # Printing the stars in the row.
            print("*" * i, end="")
            
            # Printing the spaces in the row.
            print(" " * iniS, end="")
            
            # Printing the stars in the row.
            print("*" * i)
            
            """ The spaces decrease by 2 
            every time we hit a new row."""
            iniS -= 2

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern19(N)
