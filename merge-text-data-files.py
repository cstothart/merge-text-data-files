""" Vertically stack all text data files (either tab-delimited or csv) in a given directory.

"""

import argparse

def get_dir_path():
    desc = 'Vertically stack all text data files (either tab-delimited or csv) \
        in a given directory.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('path', help='directory path containing the text files')
    args = parser.parse_args()
    return(args.path)

def main():
    path = get_dir_path()

if __name__ == '__main__':
    main()