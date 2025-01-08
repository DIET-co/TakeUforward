class Solution:
    # Function to print pattern12
    def pattern12(self, n):
        # Initial no. of spaces in row 1.
        spaces = 2 * (n - 1)

        # Outer loop for the number of rows.
        for i in range(1, n + 1):
            # For printing numbers in each row
            for j in range(1, i + 1):
                print(j, end="")

            # For printing spaces in each row
            for j in range(1, spaces + 1):
                print(" ", end="")

            # For printing numbers in each row
            for j in range(i, 0, -1):
                print(j, end="")

            """ As soon as the numbers for each iteration
            are printed, we move to the next row and give
            a line break otherwise all numbers would get 
            printed in 1 line"""
            print()

            """ After each iteration nos. increase by 
            2, thus spaces will decrement by 2"""
            spaces -= 2

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern12(N)
