""" Vertically merge tab-delimited and/or comma-delimited (CSV) text files.

Vertically merges all text files in a given directory. Can be a combination 
of tab-delimited and comma-delimeted text files. Resulting file can be tab- 
or comma-delimited regardless of the type of files that were merged.


"""

import argparse
import glob
import os


class FileMerger:

    def __init__(self):
        try:
            self.args = self._get_args()
        except FileNotFoundError as e:
            print(e)
            raise SystemExit
        self.out_delim = ',' if(self.args.csv) else '\t'
        self.file_col = self.args.file_col
        self.no_headers = self.args.no_headers
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
        parser.add_argument('in_path', 
                            help='path to directory containing text files')
        parser.add_argument('out_path', 
                            help='Output file name')
        parser.add_argument('--csv', 
                            help='Make output comma-delimited (CSV)', 
                            action='store_true')
        parser.add_argument('--no_headers', 
                            help='Use if input files do not have headers',
                            action='store_true')                               
        parser.add_argument('--file_col', 
                            help='Add column with file paths to the output \
                                  file', 
                            action='store_true')                  
        args = parser.parse_args()
        if(not os.path.isdir(args.in_path)):
            raise FileNotFoundError('Unable to find directory: {}'
                                    .format(args.in_path))
        else:
            return(args)

    def _get_file_paths(self, dir_path):
        print('Looking for text files in ' +  dir_path)    
        file_paths = (glob.glob(os.path.join(dir_path, '*.txt')) + 
                      glob.glob(os.path.join(dir_path, '*.csv')))
        print('Found {} files to process'.format(str(len(file_paths))))
        return file_paths 
        
    def _process_file(self, file_path, index):
        print('Processing {}'.format(file_path))
        file = open(file_path, 'r')
        first_row = True
        for in_row in file:
            if first_row:
                first_row = False
                if index > 0 and not self.no_headers:
                    pass
                else:
                    out_row = self._process_row(in_row, file_path, True)
                    self.out_file.write(out_row)
            else:
                out_row = self._process_row(in_row, file_path, False)
                self.out_file.write(out_row)
        file.close()        

    def _process_row(self, in_row, file_path, header):
        in_delim = ',' if file_path.find(".csv") >= 0 else '\t'
        out_row = in_row.split(in_delim)
        if self.file_col:
            out_row = self.out_delim.join(out_row).strip()
            if header and not self.no_headers:
                out_row = out_row + self.out_delim + 'file_path\n'
            else:
                out_row = out_row + self.out_delim + file_path + '\n'             
        else:
            out_row = '{}\n'.format(self.out_delim.join(out_row).strip())
        return out_row


if __name__ == '__main__':
    fm = FileMerger()
    fm.process_files()