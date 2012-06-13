#!/usr/bin/python

import oauth2
import simplejson as json
from pprint import pprint


CLIENT_ID="KLYMIDVS5MBPF2LJTYW5NTP4C5A1LPK1QJ0WM50EJ5IND14K"
CLIENT_SECRET="G41YPP12KH1L4GZEPKGDDBBDYN1GDMBTTR0OTJPSTXJM1NTO"
OATH_BASE="http://foursquare.com"
CALLBACK_URL="http://unsure.org"
CODE = 'NU2FF3VFNGYL3BUZBSW3TVYZY0IULVVQNNVDY4RB0PTWWJ3P'
ACCESS_TOKEN='SE2MSPDE3DW1USZU5GOCX3MND50G5Y20SI3X31XOYLNTFFJB'

c = oauth2.Client2(CLIENT_ID, CLIENT_SECRET, OATH_BASE)

(headers, content) = c.request('https://api.foursquare.com/v2/users/self', access_token=ACCESS_TOKEN)
if headers['status'] != '200':
	raise Exception(content)
response = json.loads(content)["response"]

print response['user']['mayorships']