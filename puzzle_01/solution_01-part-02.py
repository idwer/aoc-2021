import sys


def do(file):
    index = 0
    increased = 0

    with open(file) as infile:
        rows = [int(n) for n in infile.read().splitlines()]

        for line, _ in enumerate(rows):
            sum_window_first = sum(rows[index:index + 3])

            index += 1

            sum_window_second = sum(rows[index:index + 3])

            if sum_window_first < sum_window_second:
                increased += 1

    print(f"solution: {increased}")


if __name__ == '__main__':
    do(sys.argv[1])
