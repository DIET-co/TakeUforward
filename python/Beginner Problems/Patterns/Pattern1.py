# Pattern1.py

def print_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    n = 5  # You can change this value to print more or fewer rows
    print_pattern(n)
    