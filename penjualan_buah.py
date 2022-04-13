import sys
import operator

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <sold: dict(str, int)>")
        print("Description: Get best selling item")
        print(f"Example: {sys.argv[0]} durian: 10, apel: 10, mangga: 20, jeruk: 30, pepaya: 10")
        exit()

    if (len(sys.argv) < 2):
        print(f"Missing k, or n value, try executing just '{sys.argv[0]}' to see help")
        exit()

    try:
        items = [[x for x in ss.split(":")] for ss in "".join(sys.argv[1:]).split(",")]
        items = [(item[0], int(item[1])) for item in items]
        items = dict(items)

        key_of_max_element = max(items.items(), key=operator.itemgetter(1))[0]

        print(f"{key_of_max_element}: {items[key_of_max_element]}")

    except ValueError:
        print("Invalid parameter: please use integers")
