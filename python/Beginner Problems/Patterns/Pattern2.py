class Solution:
    
    # Function to print pattern2
    def pattern2(self, n):
        
        # Outer loop will run for rows.
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(i+1):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 10

        # Create an instnce of the Solution class
        sol = Solution()

        sol.pattern2(N)
        
        # Call the main method
if __name__ == "__main__":
 Solution().main()
