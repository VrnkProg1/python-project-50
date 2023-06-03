import argparse
from gendiff.generate import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def main():
    args = parse_args()
    first_file, second_file = args.first_file, args.second_file

    generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
