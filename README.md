# Telescraper


## Install

Install telescraper and required dependencies on first run:
````
git clone https://github.com/latsku/telescraper.git
cd telescraper
virtualenv env
source env/bin/activate
pip install -r requirements.txt
````

## Usage

Activate the python virtualenv:
````
source env/bin/activate
````

### Downloading messages from Telegram chat:

````
./telescraper.py

Found following chats/groups/channels:
            777000 Telegram
        1234567890 latsku
Select chat/group/channel by id (like -1001234567890): 1234567890

[{"id": 582, "date": "2022-03-14T15:32:22Z", "text": "Example Telegram message"}]
````


### List Help

````
./telescraper.py -h
usage: telescraper.py [-h] [--id TARGET_ID] [--list]

Scrape Telegram messages.

optional arguments:
  -h, --help      show this help message and exit
  --id TARGET_ID  Scraped chat, group, or channel id
  --list          Only list chat, group, and channel ids

````