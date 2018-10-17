from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
uh = urlopen(url, context=ctx).read()

tree = ET.fromstring(uh)
results = tree.findall('comments/comment')
count =0
sum=0

for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x

print ("Count : ",count)
print ("Sum : ",sum)
