import argparse



def main():

    parser = argparse.ArgumentParser(prog='Вычислитель отличий',
                                     description='Compares two configuration files and shows a difference.'
                                     )
    
   
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f','--format',help='set format of output')


    args = parser.parse_args()


if __name__ == "__main__":
    main()