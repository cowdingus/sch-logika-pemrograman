import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <n: integer[]>")
        print("Description: Check if the array given is unique")
        print(f"Example: {sys.argv[0]} 1, 2, 3, 4, 5")
        exit()

    if (len(sys.argv) < 2):
        print(f"Missing k, or n value, try executing just '{sys.argv[0]}' to see help")
        exit()

    try:
        numbers = "".join(sys.argv[2:]).strip().replace("[", "").replace("]", "").split(",")
        numbers = [int(x) for x in numbers]

        for i in range(len(numbers)):
            for y in range(len(numbers)):
                if i == y: continue

                if numbers[i] == numbers[y]:
                    print("Not Unique")
                    exit()

                pass

        print("Unique")

    except ValueError:
        print("Invalid parameter: please use integers")
