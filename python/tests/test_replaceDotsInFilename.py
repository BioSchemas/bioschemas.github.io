import unittest

from simplifyJSON import replaceDotsInFilename

class TestReplaceDotsInFilename(unittest.TestCase):
    def test_replaceDotsInFilename1(self):
        """
        Test correct replacement of `.` with `-`
        """
        result = replaceDotsInFilename("ComputationalTool_v1.0-RELEASE.json")
        self.assertEqual(result, "ComputationalTool_v1-0-RELEASE.json")
    def test_replaceDotsInFilename2(self):
        """
        Test correct replacement of `.` with `-`
        """
        result = replaceDotsInFilename("Computational.Tool.json_v1.0-RELEASE.json")
        self.assertEqual(result, "Computational-Tool-json_v1-0-RELEASE.json")

if __name__ == "__main__":
    unittest.main()
