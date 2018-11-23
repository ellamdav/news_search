from unittest import TestCase

from query_normaliser import QueryNormaliser


class TestQueryNormaliser(TestCase):

    def setUp(self):
        self.sut = QueryNormaliser()

    def test_normalise_concatenates_query_with_hyphens(self):
        self.assertEqual('AND-a-b-c', self.sut.normalise('AND', ['a', 'b', 'c']))

    def test_normalise_uppercases_operator(self):
        self.assertEqual('AND-a-b-c', self.sut.normalise('and', ['a', 'b', 'c']))

    def test_normalise_lowercases_search_terms(self):
        self.assertEqual('AND-a-b-c', self.sut.normalise('AND', ['A', 'b', 'C']))

    def test_normalise_sorts_search_terms(self):
        self.assertEqual('AND-a-b-c', self.sut.normalise('AND', ['C', 'b', 'A']))