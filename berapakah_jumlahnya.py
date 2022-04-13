import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <n: integer>")
        print("Description: Sum numbers from 1 to N")

    try:
        input = int(sys.argv[1])

        sum = 0

        for i in range(0, input + 1):
            sum += i

        print(sum)
    except ValueError:
        print("Invalid parameter: please use integer")
