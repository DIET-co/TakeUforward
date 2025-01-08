class Solution:
    #Function to print pattern10
    def pattern10(self, n):
        # Outer loop for number of rows.
        for i in range(1, 2 * n):
            
            """ stars would be equal to the
            row no. uptill first half"""
            stars = i if i <= n else 2 * n - i
            
            # for printing the stars in each row.
            for j in range(1, stars + 1):
                print("*", end="")
            
            """ As soon as the stars for each iteration are 
            printed, we move to the next row and give a line break"""
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern10(N)
