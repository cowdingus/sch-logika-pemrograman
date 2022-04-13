import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <integer> [..., integer]")
        print("Description: Check the evenness of the numbers given")
        exit()

    try:
        numbers = "".join(sys.argv[1:]).strip().split(",")
        numbers = [int(x) for x in numbers]

        print("[", end="")
        for i in range(0, len(numbers)):
            print("Odd" if numbers[i] % 2 else "Even", end=(", " if i != (len(numbers) - 1) else ""))
        print("]")

    except ValueError:
        print("Invalid parameter: please use integer")
