import argparse

from file_based_document_store import IndexedFileBasedDocumentStore
from query_normaliser import QueryNormaliser

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--operator', nargs='?', default='OR', help='AND|OR operator (default OR)')
parser.add_argument('-d', '--document', action='store_true', help='show document(s) instead of just id(s)')
parser.add_argument('search_term', nargs='+')
args = parser.parse_args()


query_normaliser = QueryNormaliser()
normalised_query = query_normaliser.normalise(args.operator, args.search_term)

document_store = IndexedFileBasedDocumentStore()
document_store.initialize('data/hscic-news.txt')

matching_ids = document_store.query(normalised_query)

if args.document:
    for id in matching_ids:
        print document_store.fetch(id)
else:
    print matching_ids
