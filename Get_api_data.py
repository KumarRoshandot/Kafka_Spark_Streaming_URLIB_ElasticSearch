import urllib.request, urllib.parse, urllib.error
import ssl


class get_api():

    def __init__(self):
        print("API DATA")

    def print_api_data(self, msg):
        print(msg)

    def get_data(self, url):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        #url = 'http://worldclockapi.com/api/json/est/now'

        fhand = urllib.request.urlopen(url, context=ctx)
        for line in fhand:
            data = line.decode().strip()
            return data





