import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <integer>")
        print("Description: Check if the number is even or odd")
        exit()

    try:
        input = int(sys.argv[1]);

        print("Odd" if input % 2 else "Even")
    except ValueError:
        print("Invalid parameter: please use integer")
