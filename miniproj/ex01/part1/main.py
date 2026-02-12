import sys

from checkmate import checkmate

def main():
    if len(sys.argv) == 1:
        print("You must input file name at least one argument.")
    else:
        for i in range(1, len(sys.argv)):
            with open(sys.argv[i], "r") as f:
                data = f.read().replace("\n", " ")
                checkmate(data)

if __name__ == "__main__":
    main()
