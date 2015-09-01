# HTML Quote Miner is simple Script that finds all quoted text from HTML file

"""html_quote_miner: Extracts Quotes from HTML text"""
__version__ = "1.1"
__author__ = "Sidharth Shah (sidharth@fafadiatech.com)"
__copyright__ = "(C) 2015 Sidharth Shah. GNU GPL 3."

import re
import sys
import requests
import commands

if len(sys.argv) < 2:
    print "Please specify URL to check quote from"
    sys.exit(-1)

url = sys.argv[1]
response = requests.get(url)

if response.status_code != 200:
    print "Error fetching url:%s" % url

file_to_save = open("data.html", "w")
file_to_save.write(response.text)
file_to_save.close()

CMD = "lynx -dump data.html > data.txt"
s,o = commands.getstatusoutput(CMD)

for matching_element in re.finditer(r"\".*\"\s+", open("data.txt").read(), re.IGNORECASE):
    print matching_element.group()
