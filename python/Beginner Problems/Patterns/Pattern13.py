class Solution:
    # Function to print pattern13
    def pattern13(self, n):
        # starting the number
        num = 1

        # Outer loop for the number of rows.
        for i in range(1, n + 1):
            
            """ Inner loop will loop for i times and
            print numbers increasing by 1 each time"""
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1
                
            """ As soon as the numbers for each iteration
            are printed, we move to the next row and give
            a line break otherwise all numbers would get
            printed in 1 line"""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern13(N)
