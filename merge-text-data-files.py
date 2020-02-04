""" Vertically stack all text data files (either tab-delimited or CSV) in a
given directory.

Assumes the first row of each file contains the column headings. Skips this 
row for all but the first file added to the output file.

"""

import argparse
import glob
import os

def get_args():
    desc = 'Vertically stack all text data files (either tab-delimited or CSV) \
        in a given directory.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('in_path', help='path to directory containing text \
                        files')
    parser.add_argument('out_path', help='output file pathname (for example, \
                        merged.txt)')
    parser.add_argument('--csv', help='make output CSV', action='store_true')
    parser.add_argument('--file_col', help='add column with file names to \
                        the output file', action='store_true')                    
    args = parser.parse_args()
    return(args)

def get_file_paths(dir_path):
    print('looking for text files in ' +  dir_path)    
    file_paths = (glob.glob(os.path.join(dir_path, '*.txt')) + 
                  glob.glob(os.path.join(dir_path, '*.csv')))
    print('found ' + str(len(file_paths)) + ' files to process')
    return(file_paths)

def process_file(file_path, index, out_delim, file_col):
    print('processing ' + file_path)
    file = open(file_path, 'r')
    first_row = True
    for row in file:
        if first_row:
            first_row = False
            if index > 0:
                pass
            else:
                if file_col:
        else:
            print(row)
    file.close()

def main():
    args = get_args()
    if(not os.path.isdir(args.in_path)):
        print('unable to find directory: ' + str(args.in_path))
        exit()
    out_delim = ',' if(args.csv) else '\t'
    file_paths = get_file_paths(args.in_path)
    out_file = open(args.out_path, 'w')
    for file_path in file_paths:
        process_file(file_path, 
                     file_paths.index(file_path), 
                     out_delim, 
                     args.file_col)
    out_file.close()

if __name__ == '__main__':
    main()