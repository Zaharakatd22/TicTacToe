def main():
    cells = input("Enter cells: > ")
    print("---------")
    curr_row = 1
    curr_symbol = 0
    for elem in cells:
        curr_symbol += 1
        if curr_symbol % 3 == 0:
            print(elem + " ", end="")
            print("|")
            curr_row += 1
        elif (curr_symbol - 1) % 3 == 0:
            print("| ", end="")
        if curr_symbol % 3 > 0:
            print(elem + " ", end="")

    print("---------")


if __name__ == "__main__":
    main()
