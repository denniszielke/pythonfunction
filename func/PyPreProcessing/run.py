import os
import sys
import json
import datetime
import platform
# See sample code https://github.com/yokawasa/azure-functions-python-samples

postreqdata = json.loads(open(os.environ['req']).read())
print(postreqdata)
message = "Using python '{0}'".format(platform.python_version())
print(message)
datestring = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(datestring)

outdocevent= {
    "name": postreqdata['name'], 
    "timestamp": datestring,
    "invocationid": os.environ['invocationId'],
    "data": postreqdata['data']
}

outdocdb= {
    "name": postreqdata['name'], 
    "timestamp": datestring,
    "invocationid": os.environ['invocationId'],
    "data": postreqdata['data']
}

# Writing to event hub
print('Writing eventhub:', outdocevent)
with open(os.environ['outdocevent'], 'wb') as f:
    json.dump(outdocevent,f)

# Writing to docdb
print('Writing outdocdb:', outdocdb)
with open(os.environ['outdocdb'], 'wb') as f:
    json.dump(outdocdb,f)
