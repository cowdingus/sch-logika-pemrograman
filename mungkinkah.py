import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <k: integer> <n: integer[]>")
        print("Description: Check if you can get `k` by adding two of the numbers inside n")
        print(f"Example: {sys.argv[0]} 5 '[1, 3, 4]'")
        exit()

    if (len(sys.argv) < 2):
        print(f"Missing k, or n value, try executing just '{sys.argv[0]}' to see help")
        exit()

    try:
        k = int(sys.argv[1])
        n = "".join(sys.argv[2:]).strip().replace("[", "").replace("]", "").split(",")
        n = [int(x) for x in n]

        for i in range(len(n)):
            for y in range(len(n)):
                if i == y: continue

                if n[i] + n[y] == k:
                    print("Bisa")
                    exit()

                pass

        print("Tidak Bisa")

    except ValueError:
        print("Invalid parameter: please use integers")
