import oembed
import pprint
import json
from urllib.parse import urlparse

import requests
import tldextract as tld
import urllib.parse


# 인스타
def getCreds():
    creds = dict()
    creds[
        'access_token'] = 'EAAPYXZBtgsY4BAEkRwybNpZBFQSoCZCseY5sWskgyyQuLgJObgLyZBPwuxWeZAOssZAFg6aLq1ZBZCJZBpZCONRAhZBslGRl5FbsVhoR0d0ZBZCbX3x0CKMaBocMwpCxWnXtm5z6aLGn2l3JT1wLZCv5OBwNkBkzIynJ35wmnbnpQHuLsYbis3YGwh1tRZBh2q29821GADd54rOIMad8HtztBwZAZCW3ZC'
    creds['client_id'] = '1082331412607374'
    creds['client_secret'] = 'acfda3337862fc04910360cef8258bc4'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'

    return creds


def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)

    response = dict()
    response['url'] = url


# url = "https://www.youtube.com/watch?v=dBD54EZIrZo"
# url = "https://www.instagram.com/p/BUawPlPF_Rx/"
# url = "https://twitter.com/hellopolicy/status/867177144815804416"
# url = "https://play.tvcf.co.kr/856982"
# vurl = "https://vimeo.com/20097015"
# url = "http://www.flickr.com/photos/wizardbt/2584979382/"
url = "https://www.instagram.com/lckofficial/p/CYoeOUpvY7v/"
# url = "https://youtu.be/xveSO_eh0ag"

tld = tld.extract(url).domain

# domain = urlparse(url).netloc
# rm_www = domain.replace('www.', '')

# print(rm_www)
# exit()

# json 파일 열기
with open('distros.json', 'r') as f:
    distros_dict = json.load(f)

# 데이터 가져오기
for distro in distros_dict:
    # if domain in distro['provider_url']:
    if tld in distro['provider_url']:
        # print(distro['endpoints'][0].get('schemes')[0])
        # print(distro['endpoints'][0].get('url'))

        this_scheme_arr = distro['endpoints'][0].get('schemes')
        scheme_url = distro['endpoints'][0].get('schemes')[0]

        if tld == "instagram":
            endpoint_url = distro['endpoints'][0].get(
                'url') + "?url=" + url + "&access_token=IGQVJVakw0RGdpLWtCR1JsbGRtTjhyRG1pYng3RTR1M1RaTE83WUJidzRpdldGSG1JRFVQNXdiejd3UVJVMXJwUzNvRW5uZAENGcnFEWjRHQzNydkRYelE4NmpGM0tQSkZA6WVgyUmVtUTEzSDNzQUN5cQZDZD"
        else:
            endpoint_url = distro['endpoints'][0].get('url')


consumer = oembed.OEmbedConsumer()
#
# endpoint = oembed.OEmbedEndpoint(endpoint_url, \
#                                  [scheme_url])
# consumer.addEndpoint(endpoint)
# response = consumer.embed(url)

# pprint.pprint(response.getData())

for i in this_scheme_arr:
    try:
        # 재도전
        endpoint = oembed.OEmbedEndpoint(endpoint_url, \
                                         [i])
        consumer.addEndpoint(endpoint)
        response = consumer.embed(url)

        pprint.pprint(response.getData())
    except:
        print("nothing??")

# 인스타 빼고 다 된다 ㅠ 에휴 -> 앱 검수를 해야함?
# print(response['url'])
