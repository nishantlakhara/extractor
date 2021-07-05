import requests
import time

jokes = ['aur', 'priyanka', 'kaisi', 'hai']
# jokes = range(100)

# for joke in jokes:
#     print(joke)
#     base_url = 'https://api.telegram.org/bot1871862476:AAHGyBeVpAqOxP7oKPh1o1uqC9jsCZnBrQc/sendMessage?chat_id=-1001439795216&text={}'.format(joke)
#     print(base_url)
#     time.sleep(5)
#     requests.get(base_url)

image_url =  "http://assets.myntassets.com/assets/images/13862504/2021/3/19/67044836-6c57-4020-952c-d08e765526401616139597688-BOULT-AUDIO-Black-True-Wireless-AirBass-Combuds-Bluetooth-He-1.jpg"
send_photo_url = f'https://api.telegram.org/bot1871862476:AAHGyBeVpAqOxP7oKPh1o1uqC9jsCZnBrQc/sendPhoto?chat_id=-1001439795216&photo={image_url}&caption=Telegra_logo'
requests.post(send_photo_url)