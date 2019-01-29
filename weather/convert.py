"""
weather file xml -> json
ref : github/martinblech/xmltodict
"""

import xmltodict
import json
import sys
def main():
    """single function"""
    xml = open(sys.argv[1], "r").read()
    jsn = open("weather.json", "w")
    jsn.write(json.dumps(xmltodict.parse(xml, attr_prefix='')['current'], indent=2))
    jsn.close
    print("weather.json")

main()