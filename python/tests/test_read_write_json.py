import unittest

from os.path import exists
from simplifyJSON import readJSONFile, writeJSONFile

class TestReadWriteJSONFile(unittest.TestCase):
    def test_readJSONFile(self):
        """
        Test ability to read a JSON file
        """
        result = readJSONFile('./tests/test_file.json')
        self.assertEqual(len(result), 2)

    def test_writeJSONFile(self):
        """
        Test ability to write a JSON file
        """
        writeJSONFile(['foo', {'bar': ('baz', None, 1.0, 2)}])
        self.assertTrue(exists('test.json'))

    # TODO: Write more tests

if __name__ == "__main__":
    unittest.main()
