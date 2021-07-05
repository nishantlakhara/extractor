import requests
import urllib
import logging

logging.basicConfig(level=logging.DEBUG)

import browser_cookie3

import requests

cookies_obj = browser_cookie3.chrome(domain_name='.cuelinks.com')
cookies = {}
for cookie in cookies_obj:
    cookies[cookie.name] = cookie.value
print(cookies)

landingPage_url = ""
try:
    cuelinks_url = "https://www.cuelinks.com/shorten_link?url=" + urllib.parse.quote_plus(landingPage_url)
    print(cuelinks_url)
    response = requests.get(cuelinks_url, cookies=cookies)
    print(response)
    print(response.text)

except Exception as e:
    print("ignore", e)