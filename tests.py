import unittest

from main import get_words, get_anagrams, delete_when_one


class MyTestCase(unittest.TestCase):
    def test_get_words(self):
        self.assertEqual(338882, len(get_words()))  # add assertion here

    def test_get_anagrams(self):
        result = get_anagrams(["CAT","ATC","TCP"])
        expected = {'ACT': 'CAT,ATC', 'CPT': 'TCP'}
        self.assertEqual(expected,result)

    def test_delete_when_one(self):
        result = delete_when_one({'ACT': 'CAT,ATC', 'CPT': 'TCP'})
        self.assertEqual({'ACT': 'CAT,ATC'},result)
if __name__ == '__main__':
    unittest.main()
