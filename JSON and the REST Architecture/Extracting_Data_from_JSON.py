#from urllib.request import urlopen
import urllib,json

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1: break

    print ('Retrieving ',url)
    data = urllib.urlopen(url).read()

    print ('Retrieved',len(data),'characters')
    json_data = json.loads(str(data))
    #print json.dumps(json_data['comments'], indent=3)

    comment_count = len(json_data['comments'])
    print ('Count:',comment_count)

    comment_sum = 0
    for comment in json_data['comments']:
        comment_sum = comment_sum + int(comment['count'])
    print ('Sum:',comment_sum)
