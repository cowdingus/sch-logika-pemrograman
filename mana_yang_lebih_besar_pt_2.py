import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <n: integer> [..., n]")
        print("Description: Get the maximum number in specified list of n")
        print(f"Example: {sys.argv[0]} 1, 5, 3, 6, 2")
        exit()

    try:
        numbers = "".join(sys.argv[1:]).strip().split(",")
        numbers = [int(x) for x in numbers]

        print(max(numbers));
    except ValueError:
        print("Invalid parameter: please ensure every elements of input is an integer")
