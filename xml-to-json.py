from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
from json import dumps
str = open('demographics.xml', 'r').read()
print(dumps(bf.data(fromstring(str))))

