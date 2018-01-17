import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="provide the url with RADAMSA string to use as fuzzing")
parser.add_argument("count",help="privide the numer of probes to be  send", type=int)
parser.add_argument("--custom_headers",help="custom header")
args = parser.parse_args()
#print args.url

custom_headers = {'user-agent':'Firefox / fake - radamsa'}
#custom_payload = {'data':'data'}

# add http:// if not provided as url

if args.url.startswith("http"):
	url = args.url
else:
	url = 'http://'+args.url

# replace RADAMSA with fuzzed value

for i in range(1,args.count):
	r = requests.get(url+'/'+`i`,headers=custom_headers)
	print r.status_code
	print r.text


