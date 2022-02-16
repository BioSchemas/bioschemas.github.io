import json
import logging
import re # regex library
import requests

## Logging configuration
logging.basicConfig(
    filename='simplifyJSON.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG)

### GLOBAL CONSTANTS
# Define location to read DDE generated JSON files
SCHEMA_SOURCE = "https://raw.githubusercontent.com/BioSchemas/specifications/master/"
# Define location to write simplified JSON Schema files
SCHEMA_TARGET = "../_data/schemas/"

def replaceDotsInFilename(filename):
    # Replace `.` in filename with `-` except for final `.json`
    str = re.sub('\.(?!json$)', '-', filename)
    return str

def readJSONFile(url):
    logging.debug('Entering readJSONFile from %s' % url)
    r = requests.get(url)
    data = json.loads(r.text)
    logging.debug('Exiting readJSONFile – dictionary size %d' % len(data))
    return data

def writeJSONFile(data, filename):
    logging.debug('Entering writeJSONFile() with dictionary size %d and filename %s' % (len(data), filename))
    with open(filename, 'w') as f:
        json.dump(data, f)
    f.close()
    logging.debug('Exiting writeJSONFile')

#### Main
profile = "ComputationalTool"
schema_file = "ComputationalTool_v1.0-RELEASE.json"
json_data = readJSONFile(SCHEMA_SOURCE + profile + "/jsonld/" + schema_file)
new_filename = SCHEMA_TARGET + replaceDotsInFilename(schema_file)
logging.info('Filename: %s' % new_filename)
# writeJSONFile(json_data, 'test.json')
