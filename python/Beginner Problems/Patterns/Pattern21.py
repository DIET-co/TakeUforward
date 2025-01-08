class Solution:
    # Function to print pattern21
    def pattern21(self, n):
        # Outer loop for the rows.
        for i in range(n):
            
            """ Inner loop for printing 
            the stars at borders only."""
            for j in range(n):
                
                if i == 0 or j == 0 or i == n-1 or j == n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
                    
            # Move to the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern21(N)
