import json
import logging
import re # regex library

## Logging configuration
logging.basicConfig(
    filename='simplifyJSON.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG)

### GLOBAL CONSTANTS
# Define location of JSON Schema files
SCHEMA_LOC = "../_data/schemas/"

def replaceDotsInFilename(filename):
    # Replace `.` in filename with `-` except for final `.json`
    str = re.sub('\.(?!json$)', '-', filename)
    return str

def readJSONFile(filename):
    logging.debug('Entering readJSONFile with %s' % filename)
    f = open(filename)
    data = json.load(f)
    f.close()
    logging.debug('Exiting readJSONFile – dictionary size %d' % len(data))
    return data

def writeJSONFile(data, filename):
    logging.debug('Entering writeJSONFile() with dictionary size %d and filename %s' % (len(data), filename))
    with open(filename, 'w') as f:
        json.dump(data, f)
    f.close()
    logging.debug('Exiting writeJSONFile')

#### Main
filename = SCHEMA_LOC + replaceDotsInFilename("ComputationalTool_v1-0-RELEASE.json")
logging.info('Filename: %s' % filename)
json_data = readJSONFile(filename)
writeJSONFile(json_data, 'test.json')

f = open('test.json')
data = json.load(f)
for key in data.keys():
    logging.debug(key)
    print (key)
f.close()
