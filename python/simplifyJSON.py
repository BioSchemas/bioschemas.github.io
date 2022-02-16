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
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = json.loads(r.text)
            logging.debug('Exiting readJSONFile – dictionary size %d' % len(data))
            return data
        else:
            logging.error('Got a %d error code from %s' % (r.status_code, url))
            raise Exception('Got a %d error code from %s' % (r.status_code, url))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def writeJSONFile(data, filename):
    logging.debug('Entering writeJSONFile() with dictionary size %d and filename %s' % (len(data), filename))
    with open(filename, 'w') as f:
        json.dump(data, f)
    f.close()
    logging.debug('Exiting writeJSONFile')

def replace_nested_json_key(obj, key, newkey):
    """Recursively replace key/value in nested JSON."""
    logging.debug("Entering replace_nested_json_key() with key: %s, newkey: %s, and dict:\n%s" % (key, newkey, str(obj)))
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                replace_nested_json_key(v, key, newkey)
        if key in obj:
            logging.debug('Replacing %s with %s' % (key, newkey))
            obj[newkey] = obj.pop(key)
    elif isinstance(obj, list):
        for item in obj:
            replace_nested_json_key(item, key, newkey)

    logging.debug("Exiting replace_nested_json_key() with key: %s, newkey: %s, and dict:\n%s" % (key, newkey, str(obj)))
    return obj

def replaceJSONLDKey(data):
    logging.debug('Entering replaceJSONLDKey() with ' + str(data))
    replacementStrings = {'@context': 'jsonld-context',
                        '@graph': 'jsonld-graph',
                        '@id': 'jsonld-id'}
    for k, v in replacementStrings.items():
        data = replace_nested_json_key(data, k, v)
    logging.debug('Exiting replaceJSONLDKey() with ' + str(data))
    return data

#### Main
profile = "ComputationalTool"
schema_file = "ComputationalTool_v1.0-RELEASE.json"
json_data = readJSONFile(SCHEMA_SOURCE + profile + "/jsonld/" + schema_file)
new_filename = SCHEMA_TARGET + replaceDotsInFilename(schema_file)
logging.info('Filename: %s' % new_filename)
# writeJSONFile(json_data, 'test.json')
