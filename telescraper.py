#!/usr/bin/env python3
import argparse
import json

from telethon import TelegramClient

# https://docs.telethon.dev/en/stable/modules/client.html#telethon-client

# Go to https://my.telegram.org to register an app to get these.
API_ID = 12345678
API_HASH = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
APP_NAME = 'example'

async def main(target_id: int, list_only):

    if not target_id:
        print("Found following chats/groups/channels:")

        async for dialog in client.iter_dialogs():
            print("{:16} {}".format(dialog.id, dialog.name))

    if not list_only:
        if not target_id:
            target_id = int(input("Select chat/group/channel by id (like -1001234567890): "))
        msgs = list()
        # You can print the message history of any chat:
        async for message in client.iter_messages(target_id):
            msg_dict = dict()
            msg_dict["id"] = message.id
            msg_dict["date"] = message.date.strftime("%Y-%m-%dT%H:%M:%SZ")
            msg_dict["text"] = message.text
            if message.geo:
                msg_dict["geo"] = message.geo

            msgs.append(msg_dict)
        print(json.dumps(msgs))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape Telegram messages.')
    parser.add_argument('--id', dest="target_id", type=int, help="Scraped chat, group, or channel id")
    parser.add_argument('--list', action='store_true', help="Only list chat, group, and channel ids")
    args = parser.parse_args()

if API_ID == 12345678 or API_HASH == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' or APP_NAME == 'example':
    print("Change API_ID, API_HASH, and APP_NAME !!!")
    print("Go to https://my.telegram.org to register an app to get these.")
else:
    with TelegramClient(APP_NAME, API_ID, API_HASH) as client:
        client.loop.run_until_complete(main(args.target_id, args.list))
