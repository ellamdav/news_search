
class QueryNormaliser(object):

    def normalise(self, operator, search_terms):
        return '-'.join([operator.upper()] + sorted([ term.lower() for term in search_terms]))
