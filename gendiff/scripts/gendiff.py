import argparse

from ..gendiff_engine.generate_diff import generate_diff


def main():

    parser = argparse.ArgumentParser(
        prog='Вычислитель отличий',
        description='Compares two configuration files and shows a difference.'
        )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, default='stylish', help='set format of output')

    args = parser.parse_args()
    
    result = generate_diff(args.first_file, 
                           args.second_file,
                           args.format
                           )

    print(result)


if __name__ == "__main__":
    main()