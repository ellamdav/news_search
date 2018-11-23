# News search - David Ellam

## Running the script

The script was tested on Python 2.7, and can be run according to the included command-line help:
```
usage: news_search.py [-h] [-o [OPERATOR]] [-d] search_term [search_term ...]

positional arguments:
  search_term

optional arguments:
  -h, --help            show this help message and exit
  -o [OPERATOR], --operator [OPERATOR]
                        AND|OR operator (default OR)
  -d, --document        show document(s) instead of just id(s)
```
eg.
```bash
python news_search.py -o AND general population Alzheimer
```
By default, the script will return a list of matching document ids -
to return the actual document content, use the `-d` flag. 
```bash
python news_search.py -o AND general population Alzheimer -d
```

## Implementation
Absolutely no error-handling has been implemented for this toy solution - this would not be the case for production code! :-)

### Query normaliser
Converts supplied query to normalised form, ie. `<logical-operator>-<sorted-keywords>`

### Linear file-backed document store
Initial implementation - a naive O(n) solution that simply iterates over the entire document store and matches against the query

### Indexed file-backed document store
O(1) solution that builds a dict of words to document IDs and uses this to satisfy the query


