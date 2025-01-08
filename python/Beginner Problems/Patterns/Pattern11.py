class Solution:
    # Function to print pattern11
    def pattern11(self, n):
        # First row starts by printing a single 1.
        start = 1

        # Outer loop for the number of rows
        for i in range(n):
            """ If the row index is even, start 
            with 1; if odd, start with 0"""
            if i % 2 == 0:
                start = 1
                
            else:
                start = 0

            """ Alternatively print 1's and 0's 
            in each row by using inner for loop"""
            for j in range(i + 1):
                print(start, end=" ")
                start = 1 - start

            # Move to the next row and give a line break
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern11(N)
