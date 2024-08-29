import csv
import sys


def main():
    with open('customers.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
    print(sys.version_info.major)
    print(sys.version_info.minor)
    print(sys.version_info.micro)

if __name__ == '__main__':
    main()