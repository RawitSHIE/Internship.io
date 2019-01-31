"""
weather file xml -> json
ref : github/martinblech/xmltodict
"""

import xmltodict
import json
import sys
import os
def writefile(xml):
    """write json"""
    jsn = open("weather.json", "w")
    jsn.write(json.dumps(xmltodict.parse(xml, attr_prefix='')['current'], indent=2))
    jsn.close()

def readfile(argv):
    """open file"""
    try:
        return open(argv, "r").read()
    except FileNotFoundError:
        sys.exit("File doesn't exist.")

def main():
    """main function"""
    xml = readfile(sys.argv[1])
    while True:
        # if file exist
        if os.path.isfile('weather.json'):
            print("weather.json exist, want overwrite? : Yes/no (Y/n)", end="")
            option = input()
            if option.lower() == "y":
                writefile(xml)
                print("weather.json is overwritten.")
                break
            elif option.lower() == "n":
                print("Terminated")
                break
            else:
                continue
        else:
            writefile(xml)
            print("weather.json is wrote")
            break
main()
