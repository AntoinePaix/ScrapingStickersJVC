# scraping-stickers

## Description

This script allows you to download all the NoelShack images of a JVC topic.

## Prerequisite

You need BeautifulSoup to parse HTML.

`pip install bs4`

## Usage

`python3 scraping-stickers.py --url <jvc_topic_url>`

Exemple :

`python3 scraping-stickers.py --url https://www.jeuxvideo.com/forums/42-47-64138872-1-0-1-0-salaire-debutant-dev-web.htm`

This will create a folder with the name of the topic in the current directory.