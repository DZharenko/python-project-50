import argparse
from gendiff.parse_file import read_json
from gendiff.gendiff_engine.generate_diff import generate_diff


def main():

    parser = argparse.ArgumentParser(prog='Вычислитель отличий',
                                     description='Compares two configuration files and shows a difference.'
                                     )
    
   
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f','--format',help='set format of output')


    args = parser.parse_args()
    
    result = generate_diff(read_json(args.first_file), read_json(args.second_file))

    print(result)

if __name__ == "__main__":
    main()