from collections import defaultdict


class DocumentStore(object):

    def parse_query(self, query_string):
        query_tokens = query_string.split('-')
        operator = query_tokens[0]
        query_terms = query_tokens[1:]
        return operator, query_terms

    def fetch(self, id):
        return self.documents[id]


class LinearFileBasedDocumentStore(DocumentStore):

    def initialize(self, filename):
        with open(filename) as f:
            self.documents = f.read().splitlines()

    def query(self, query_string):
        operator, query_terms = self.parse_query(query_string)
        predicate = any if operator == 'OR' else all
        return [ id for id, document in enumerate(self.documents)
                 if predicate(term in document.lower() for term in query_terms)]


class IndexedFileBasedDocumentStore(DocumentStore):

    def initialize(self, filename):
        with open(filename) as f:
            self.documents = f.read().splitlines()
            self.index = self.build_index_from_documents()

    def build_index_from_documents(self):
        index = defaultdict(set)
        for id, document in enumerate(self.documents):
            for word in [w.lower() for w in document.split(' ')]:
                index[word].add(id)
        return index

    def query(self, query_string):
        operator, query_terms = self.parse_query(query_string)
        predicate = set.union if operator == 'OR' else set.intersection
        matches = [ self.index[term] for term in query_terms ]
        return sorted(list(predicate(*matches)))
