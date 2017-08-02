import os
import json
import platform

postreqdata = json.loads(open(os.environ['req']).read())
message = "Using python '{0}'".format(platform.python_version())
print(message)
response = open(os.environ['res'], 'w')
response.write("hello world from "+postreqdata['name'])
response.close()