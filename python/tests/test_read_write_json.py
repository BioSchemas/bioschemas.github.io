import unittest
import unittest.mock as unitmock

import os
from simplifyJSON import readJSONFile, writeJSONFile, replaceJSONLDKey

class TestReadWriteJSONFile(unittest.TestCase):
    @unitmock.patch('simplifyJSON.requests.get')
    def test_readJSONFile_404(self, mock_get):
        """
        Test exception thrown on 404 response
        """
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception) as context:
            readJSONFile('https://raw.githubusercontent.com/BioSchemas/test_file.json')

    @unitmock.patch('simplifyJSON.requests.get')
    def test_readJSONFile_200(self, mock_get):
        """
        Test ability to read a JSON file from GitHub
        """
        # Define mock version of raw.github.com
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{\"@context\":{\"schema\":\"http:\/\/schema.org\/\",\"rdf\":\"http:\/\/www.w3.org\/1999\/02\/22-rdf-syntax-ns#\",\"rdfs\":\"http:\/\/www.w3.org\/2000\/01\/rdf-schema#\",\"bioschemas\":\"http:\/\/discovery.biothings.io\/view\/bioschemas\/\"},\"@graph\":[{\"@id\":\"bioschemas:ComputationalTool\",\"@type\":\"rdfs:Class\",\"rdfs:comment\":\"The Life Science Tools specification provides a way to describe bioscience tools and software on the World Wide Web. It defines a set of metadata and vocabularies, built on top of existing technologies and standards, that can be used to represent such tools in Web pages and applications. The goal of the specification is to make it easier to discover. Version 1.0-RELEASE.\",\"rdfs:label\":\"ComputationalTool\",\"rdfs:subClassOf\":{\"@id\":\"schema:SoftwareApplication\"},\"$validation\":{\"$schema\":\"http:\/\/json-schema.org\/draft-07\/schema#\",\"type\":\"object\",\"input\":{\"description\":\"Specification of a consumed input.\",\"oneOf\":[{\"$ref\":\"#\/definitions\/formalParameter\"},{\"type\":\"array\",\"items\":{\"$ref\":\"#\/definitions\/formalParameter\"}}]}}}]}'

        # Test read JSON from GitHub
        result = readJSONFile('https://raw.githubusercontent.com/BioSchemas/test_file.json')
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

    def test_replaceJSONLDKey(self):
        """
        Test that json-ld strings are converted to regular keys
        """
        # Load in test data
        data = {"@context":{"schema":"http://schema.org/",
                    "rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                    "rdfs":"http://www.w3.org/2000/01/rdf-schema#",
                    "bioschemas":"http://discovery.biothings.io/view/bioschemas/"},
                "@graph":[{
                    "@id":"bioschemas:ComputationalTool",
                    "@type":"rdfs:Class",
                    "rdfs:comment":"Some comment. Version 1.0-RELEASE.",
                    "rdfs:label":"ComputationalTool",
                    "rdfs:subClassOf":{
                        "@id":"schema:SoftwareApplication"},
                    "$validation":{
                        "$schema":"http://json-schema.org/draft-07/schema#",
                        "type":"object",
                        "input":{
                            "description":"Specification of a consumed input.",
                            "oneOf":[{
                                "$ref":"#/definitions/formalParameter"},
                                {"type":"array",
                                    "items":{"$ref":"#/definitions/formalParameter"}
                                }
                            ]
                        }
                    }
                }]}

        result = replaceJSONLDKey(data)
        print(data)
        keyList = list(result.keys())
        self.assertEqual(keyList[0], 'jsonld-context')
        self.assertEqual(keyList[1], 'jsonld-graph')
        graph_data = result.get('jsonld-graph')
        print(graph_data)
        keyList = list(graph_data[0].keys())
        self.assertTrue('jsonld-id' in keyList, 'jsonld-id not in keys')
        self.assertTrue('jsonld-validation' in keyList, 'jsonld-validation not in keys')

if __name__ == "__main__":
    unittest.main()
