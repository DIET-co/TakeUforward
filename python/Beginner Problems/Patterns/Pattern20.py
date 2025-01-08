class Solution:
    # Function to print pattern20
    def pattern20(self, n):
        # Initialising the spaces.
        spaces = 2 * n - 2
        
        # Outer loop to print the row.
        for i in range(1, 2 * n):
            # Stars for first half
            stars = i
            
            # Stars for the second half.
            if i > n:
                stars = 2 * n - i
            
            # For printing the stars
            print("*" * stars, end="")
            
            # For printing the spaces
            print(" " * spaces, end="")
            
            # For printing the stars
            print("*" * stars, end="")
            
            # Give a line break for new row.
            print()
            
            # Adjust spaces for the next row
            if i < n:
                spaces -= 2
            else:
                spaces += 2

# Main function
if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern20(N)
