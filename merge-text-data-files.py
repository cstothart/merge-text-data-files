""" Vertically stack all text data files (either tab-delimited or CSV) in a
given directory.

Assumes the first row of each file contains the column headings. Skips this 
row for all but the first file added to the output file.

"""

import argparse
import glob
import os

class NoDirectoryError(Exception):
    pass

class FileMerger:

    def __init__(self):
        try:
            self.args = self._get_args()
        except NoDirectoryError as e:
            print(e)
        self.out_delim = ',' if(self.args.csv) else '\t'
        self.file_col = True if(self.args.file_col) else False
        self.file_paths = self._get_file_paths(self.args.in_path)
        self.out_file = open(self.args.out_path, 'w')

    def process_files(self):
        for file_path in self.file_paths:
            self._process_file(file_path, self.file_paths.index(file_path))
        self.out_file.close()        

    def _get_args(self):
        desc = 'Vertically stack all text data files (either tab-delimited \
                or CSV) in a given directory.'
        parser = argparse.ArgumentParser(description=desc)
        parser.add_argument('in_path', help='path to directory containing \
                            text files')
        parser.add_argument('out_path', help='output file pathname (for \
                            example, merged.txt)')
        parser.add_argument('--csv', 
                            help='make output CSV', 
                            action='store_true')
        parser.add_argument('--file_col', help='add column with file names to \
                            the output file', action='store_true')                    
        args = parser.parse_args()
        if(not os.path.isdir(args.in_path)):
            raise NoDirectoryError('unable to find directory: ' + 
                                   str(args.in_path))
        else:
            return(args)

    def _get_file_paths(self, dir_path):
        print('looking for text files in ' +  dir_path)    
        file_paths = (glob.glob(os.path.join(dir_path, '*.txt')) + 
                      glob.glob(os.path.join(dir_path, '*.csv')))
        print('found ' + str(len(file_paths)) + ' files to process')
        return(file_paths)        

    def _process_file(self, file_path, index):
        print('processing ' + file_path)
        file = open(file_path, 'r')
        first_row = True
        for in_row in file:
            if first_row:
                first_row = False
                if index > 0:
                    pass
                else:
                    out_row = self._process_row(in_row)
            else:
                print(in_row)
        file.close()        

    def _process_row(self, in_row):
        pass

def main():
    fm = FileMerger()
    fm.process_files()

if __name__ == '__main__':
    main()