import requests
import json

def get_download_link(download_url):
    url = "https://3000-riadazz-instagramvideod-gv2sb0zwzs1.ws-us106.gitpod.io/"

    # payload = "[\"https://www.instagram.com/reel/CzgpIVKxCjm/?igshid=ODhhZWM5NmIwOQ%3D%3D\"]"
    payload = f"[\"{download_url}\"]"
    # print(f"payload: {payload}")
    headers = {
      'authority': '3000-riadazz-instagramvideod-gv2sb0zwzs1.ws-us106.gitpod.io',
      'accept': 'text/x-component',
      'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'text/plain;charset=UTF-8',
      'cookie': 'gp-necessary=true; gp-analytical=true; gitpod-marketing-website-visited=true; ajs_anonymous_id=05bd525e-b897-4099-9a7f-c94096b666de; _gitpod_io_ws_a53582a9-f4a4-4d78-b164-320acc17b22f_owner_=xTqh.1iUhUhivJCW9ju5U0JTZmMjt67x; _gitpod_io_ws_03ef1691-b37d-4f67-a15b-c33b75383035_owner_=pu1_YmgiYSXwvYh4m7wTYyflfAqhG-aF',
      'dnt': '1',
      'next-action': '6bffb1d566f7589fc69eda3797c2bf669e72a3ac',
      'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
      'next-url': '/',
      'origin': 'https://3000-riadazz-instagramvideod-gv2sb0zwzs1.ws-us106.gitpod.io',
      'referer': 'https://3000-riadazz-instagramvideod-gv2sb0zwzs1.ws-us106.gitpod.io/',
      'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response)
    return response.text.split(":\"")[5][:-4]

#Read json from "./reellist.json"
reel_list = []
with open("./reellist.json", "r") as f:
    reel_list = json.load(f)

reels  = reel_list['reels']
count = 0
for reel in reels:
    print(f"Downloading {reel}")
    try:
        download_link = get_download_link(reel)
        count = count + 1
    except:
        print(f"Failed to download {reel}")
        continue
    response = requests.get(download_link)
    with open(f"./reels/{reel.split('/')[4]}.mp4", "wb") as f:
        f.write(response.content)

    print(f"Downloaded [{count}] ./reels/{reel.split('/')[4]}.mp4")


