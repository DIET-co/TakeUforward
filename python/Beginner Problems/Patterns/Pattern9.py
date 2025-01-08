class Solution:
    def pattern9(self, n):
        self.erect_pyramid(n)
        self.inverted_pyramid(n)

    def erect_pyramid(self, n):
        # Outer loop which will loop for the rows.
        for i in range(n):
            # For printing the spaces before stars in each row
            for j in range(n - i - 1):
                print(" ", end="")

            # For printing the stars in each row
            for j in range(2 * i + 1):
                print("*", end="")

            # For printing the spaces after stars in each row
            for j in range(n - i - 1):
                print(" ", end="")

            # As soon as the stars for each iteration are printed,
            # we move to the next row and give a line break
            print()

    def inverted_pyramid(self, n):
        # Outer loop which will loop for the rows.
        for i in range(n):
            # For printing the spaces before stars in each row
            for j in range(i):
                print(" ", end="")

            # For printing the stars in each row
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")

            # For printing the spaces after stars in each row
            for j in range(i):
                print(" ", end="")

            """ As soon as the stars for each iteration are printed,
            we move to the next row and give a line break"""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern9(N)
