class Solution:
    
    # Function to print pattern3
    def pattern3(self, n):
        
        # Outer loop will run for rows.
        for i in range(1,n+1):
            
            # Inner loop will run for columns.
            for j in range(1,i+1):
                print(j, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern3(N)

if __name__ == "__main__":
    Solution().main()