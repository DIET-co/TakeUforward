class Solution:
    
    # Function to print pattern7
    def pattern7(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            #This loop will print the spaces
            for j in range(0, (n-i-1)):
                print(" ",end="")
            
            # This loop will print asterisk.
            for j in range(0,2*i+1):
                print("*", end="")

            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern7(N)

if __name__ == "__main__":
    Solution().main()
