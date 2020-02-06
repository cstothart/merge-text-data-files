# Vertically merge tab-delimited and/or comma-delimited (CSV) text files.

## Description

Vertically merges all text files in a given directory. Can be a combination 
of tab-delimited and comma-delimeted text files. Resulting file can be made 
tab-delimited or comma-delimited regardless of the type of files that were 
merged.

## Usage:

```
python merge-text-files.py in-path out-path [--csv] [--no_headers] [--file_col]
```

## Typical Usage Example:

```
python merge-text-files.py folder-with-files merged-file.txt
```

## Positional Arguments:
<pre>
in_path      Path to directory containing text files.

out_path     Output file name.
</pre>

## Optional Arguments:
<pre>
--csv         Make output file comma-delimited (CSV) instead of tab-delimited.

--no_headers  Use if input files do not have headers.

--file_col    Add to output file a column containing paths to input files.
</pre>