import unittest

import os
from simplifyJSON import readJSONFile, writeJSONFile

class TestReadWriteJSONFile(unittest.TestCase):
    def test_readJSONFile(self):
        """
        Test ability to read a JSON file
        """
        result = readJSONFile('./tests/test_file.json')
        self.assertEqual(len(result), 2)
        keyList = list(result.keys())
        self.assertEqual(keyList[0], '@context')
        self.assertEqual(keyList[1], '@graph')

    def test_writeJSONFile(self):
        """
        Test ability to write a JSON file
        """
        filename = 'OzWQr1VVB7.json'
        assert not os.path.exists(filename), "File test.json already exists and would be removed by this test."
        writeJSONFile(['foo', {'bar': ('baz', None, 1.0, 2)}], filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    # TODO: Write more tests

if __name__ == "__main__":
    unittest.main()
