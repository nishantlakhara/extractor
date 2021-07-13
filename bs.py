import requests, json
from bs4 import BeautifulSoup
from pandas import DataFrame
import urllib
import time
import logging
import math
import browser_cookie3

def convertToCuelinksUrl(landingPage_url):
    cookies_obj = browser_cookie3.chrome(domain_name='.cuelinks.com')
    cookies = {}
    for cookie in cookies_obj:
        cookies[cookie.name] = cookie.value
    print(cookies)

    try:
        cuelinks_url = "https://www.cuelinks.com/shorten_link?url=" + urllib.parse.quote_plus(landingPage_url)
        print(cuelinks_url)
        response = requests.get(cuelinks_url, cookies=cookies)
        # print(response)
        # print(response.text)
        return response.json()['short_url']
    except Exception as e:
        print("ignore", e)

def sendTelegramMessages(dataframe: DataFrame):
    base_telegram_url = "https://api.telegram.org/bot1871862476:AAHGyBeVpAqOxP7oKPh1o1uqC9jsCZnBrQc/"

    for index, row in dataframe.iterrows():
        rating = math.ceil(row['rating']*10)/10
        price = row['price']
        if (rating > 4.5 and price <= 1000):
            #print(row['searchImage'], row['landingPageUrl'])
            #print(row['productName'], row['searchImage'], row['landingPageUrl'])
            image_url = row['searchImage']
            landingPage_url = f"https://myntra.com/{row['landingPageUrl']}"
            landingPage_url = convertToCuelinksUrl(landingPage_url)
            #print(f"landingPage_url = {landingPage_url}")
            productName = urllib.parse.quote_plus(row['productName'])
            caption = f"{productName}, \nRating={str(rating)}, \nPrice={str(row['price'])}, \nmrp={str(row['mrp'])}, \ndiscount={str(row['discount'])}"
            # text = f"To buy {productName} please visit url {landingPage_url}"
            text = f"To buy {productName} please visit url {convertToCuelinksUrl(landingPage_url)}"
            send_photo_url = base_telegram_url + f'sendPhoto?chat_id=-1001439795216&photo={image_url}&caption={caption}'
            send_message_url = base_telegram_url + f'sendMessage?chat_id=-1001439795216&text={text}'
            print(send_message_url)
            requests.get(send_photo_url)
            requests.get(send_message_url)
            time.sleep(100)

# Index(['landingPageUrl', 'loyaltyPointsEnabled', 'adId', 'isPLA', 'productId',
#        'product', 'productName', 'rating', 'ratingCount', 'isFastFashion',
#        'futureDiscountedPrice', 'futureDiscountStartDate', 'discount', 'brand',
#        'searchImage', 'effectiveDiscountPercentageAfterTax',
#        'effectiveDiscountAmountAfterTax', 'buyButtonWinnerSkuId',
#        'buyButtonWinnerSellerPartnerId', 'relatedStylesCount',
#        'relatedStylesType', 'productVideos', 'inventoryInfo', 'sizes',
#        'images', 'gender', 'primaryColour', 'discountLabel',
#        'discountDisplayLabel', 'additionalInfo', 'category', 'mrp', 'price',
#        'advanceOrderTag', 'colorVariantAvailable', 'productimagetag',
#        'listViews', 'discountType', 'tdBxGyText', 'catalogDate', 'season',
#        'year', 'isPersonalised', 'eorsPicksTag', 'personalizedCoupon',
#        'personalizedCouponValue', 'productMeta', 'systemAttributes',
#        'attributeTagsPriorityList', 'preferredDeliveryTag'],
#       dtype='object')




def main():
    logging.basicConfig(level=logging.DEBUG)

    urls = ["https://www.myntra.com/flat-70-sale",
            "https://www.myntra.com/flat-70-sale?p=2&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=3&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=4&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=5&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=6&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=7&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=8&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=9&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=10&plaEnabled=false",
            "https://www.myntra.com/flat-70-sale?p=11&plaEnabled=false",
            ]

    # urls = ["https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=2&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=3&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=4&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=5&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=6&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=7&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=8&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=9&plaEnabled=false",
    #         "https://www.myntra.com/men-bags-backpacks?f=Categories%3ABackpacks&p=10&plaEnabled=false",]

    for url_main in urls:
        run_myntra_urls(url_main)


def run_myntra_urls(url_main):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    s = requests.Session()
    res = s.get(url_main, headers=headers, verify=False)
    soup = BeautifulSoup(res.text, "lxml")
    script = None
    for s in soup.find_all("script"):
        # print(f"s = {s}")
        # print(type(s))
        # print(f"s.text = {s.__str__()}")
        # if 'pdpData' in s.__str__():
        if 'searchData' in s.__str__():
            script = s.__str__().replace("<script>", "")
            script = script.replace("</script>", "")
            # print(f"script = {script}")
            break
    json_obj = json.loads(script[script.index('{'):])
    # json_formatted_str = json.dumps(json_obj, indent=2)
    dataframe = DataFrame(json_obj["searchData"]["results"]["products"])
    print(dataframe.columns)
    sendTelegramMessages(dataframe)

if __name__ == "__main__":
    main()
