from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 6248730
api_hash = '9fead66868407f41c2b2ffcf7918b129'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon1', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))