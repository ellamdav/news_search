from unittest import TestCase

from file_based_document_store import LinearFileBasedDocumentStore, IndexedFileBasedDocumentStore

TEST_DATA_FILE = '../data/hscic-news.txt'


class TestFileBasedDocumentStore():

    def test_constructor(self):
        self.assertEqual(LinearFileBasedDocumentStore, LinearFileBasedDocumentStore().__class__)

    def test_initialize(self):
        self.assertEqual(None, LinearFileBasedDocumentStore().initialize(TEST_DATA_FILE))

    def test_OR_with_no_matches_returns_empty_list(self):
        self.assertEqual([], self.sut.query('OR-foo-bar'))

    def test_OR_with_single_match_returns_expected_id(self):
        self.assertEqual([9], self.sut.query('OR-2004-september'))

    def test_OR_with_two_matches_returns_expected_ids(self):
        self.assertEqual([6, 8], self.sut.query('OR-general-population-generally'))

    def test_OR_with_many_matches_returns_expected_ids(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], self.sut.query('OR-care-commission-quality'))

    def test_AND_with_single_match_returns_expected_id(self):
        self.assertEqual([1], self.sut.query('AND-admission-care-commission-quality'))
        self.assertEqual([6], self.sut.query('AND-alzheimer-general-population'))

    def test_can_fetch_document_by_id(self):
        self.assertRegexpMatches(self.sut.fetch(5), 'Thousands of GP practices')


class TestLinearFileBasedDocumentStore(TestCase, TestFileBasedDocumentStore):

    impl = LinearFileBasedDocumentStore

    def setUp(self):
        self.sut = self.impl()
        self.sut.initialize(TEST_DATA_FILE)


class TestIndexedFileBasedDocumentStore(TestCase, TestFileBasedDocumentStore):

    impl = IndexedFileBasedDocumentStore

    def setUp(self):
        self.sut = self.impl()
        self.sut.initialize(TEST_DATA_FILE)
