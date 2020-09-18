# Coding: utf-8

# Ce script permet de collecter toutes les images noelshack d'un topic JVC

import requests
import time
import os
import argparse
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser(description="Download all noelshack images from a jvc topic.")
parser.add_argument('-u', '--url', type=str, required=True, help="URL of the first page of a jvc topic.")
args = parser.parse_args()

TOPIC_URL = args.url

def get_topic_title(topic_url):
    response = requests.get(topic_url).content
    return BeautifulSoup(response, "html.parser").title.text
 

def generate_urls(topic_url):
    topic_url = topic_url.split('-')
    i = 0
    while True:
        i += 1
        new_url = "-".join(topic_url[:3]) + "-" + str(i) + "-" + "-".join(topic_url[4:])
        time.sleep(1)
        yield new_url


urls = []
images = []
directory = get_topic_title(TOPIC_URL)

if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Création du dossier : {directory}")

for url in generate_urls(TOPIC_URL):

    response = requests.get(url)

    if response.url not in urls:
        urls.append(response.url)
        print(f"{response.url} added in urls.")

        soup = BeautifulSoup(response.content, "html.parser")

        for image in soup.find_all("img", class_="img-shack"):
            link = image['alt']
            if link not in images:
                images.append(link)

        for link in images:
            content = requests.get(link, stream=True).content
            filename = link.split("/")[-1]
            if not os.path.isfile(os.path.join(directory, filename)):
                print(f"Téléchargement de {filename}")
                with open(os.path.join(directory, filename), mode="wb") as file:
                    file.write(content)

    else:
        print(f"Fin du scraping, dernière page : {urls[-1]}")
        break