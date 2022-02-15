# Import logging
import logging
# Import regex library
import re

## Logging configuration
logging.basicConfig(
    filename='simplifyJSON.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO)

# Define location of JSON Schema files
SCHEMA_LOC = "../_data/schemas/"

def replaceDotsInFilename(filename):
    # Replace `.` in filename with `-` except for final `.json`
    str = re.sub('\.(?!json$)', '-', filename)
    return str

#### Main
filename = SCHEMA_LOC + replaceDotsInFilename("ComputationalTool_v1-0-RELEASE.json")
logging.info('Filename: %s' % filename)
