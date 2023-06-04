#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def adder(argv):
        args = sys.argv[1:]
        num = [int(arg) for arg in args]
        add = sum(num)
        print(add)

adder(sys.argv)
