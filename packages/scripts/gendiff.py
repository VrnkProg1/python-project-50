import argparse

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_argument')
parser.add_argument('second_argument')

args = parser.parse_args()

def main():
    print('a')

if __name__ == '__main__':
    main()