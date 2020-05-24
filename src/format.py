import re
import json
pattern = re.compile("(http:\/\/www\.youtube\.com\/channel\/)[A-Za-z0-9_-]+")
id = 'UUzNzJyXhVPv2jmYE3mSMhrQ'
clean = set()
for i, line in enumerate(open(id)):
    for match in re.finditer(pattern, line):
        clean.add(match.group())
        #print (f'Found on line %s: %s' % (i+1, match.group()))
        
with open(id + "clean", "a") as ff:
            json.dump(list(clean), ff)