class Solution:
    
    # Function to print pattern5
    def pattern5(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            # Inner loop will run for columns.
            for j in range(0,n-i):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern5(N)

if __name__ == "__main__":
    Solution().main()