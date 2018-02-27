import re


s = 'abc-x@gmail.com'

match = re.search(r'[\w-]+@[\w.]+',s)
if match:
    print match.group()
