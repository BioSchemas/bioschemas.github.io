# Import regex library
import re

def replaceDotsInFilename(filename):
    # Replace `.` in filename with `-` except for final `.json`
    str = re.sub('\.(?!json$)', '-', filename)
    return str

#### Main
print("../_data/schemas/" + replaceDotsInFilename("ComputationalTool_v1-0-RELEASE.json"))
