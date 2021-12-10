import os
import re
import time
import json
import requests
import threading

with open("settings.json") as fp:
    _settings = json.load(fp)
    try: th = int(os.environ["threads"])
    except: th = int(_settings.get("threads"))

    try: wait = int(os.environ["sleep"])
    except: wait = int(_settings.get("sleep"))

    try: ws = os.environ["webserver"]
    except: ws = _settings.get("webserver")

    try: wh1 = os.environ["banner"]
    except: wh1 = _settings.get("banner")

    try: wh2 = os.environ["skyscraper"]
    except: wh2 = _settings.get("skyscraper")

    try: wh3 = os.environ["square"]
    except: wh3 = _settings.get("square")

    del _settings
    fp.close()

if ws == True:
    import webserver
    webserver.start()

count1 = 0
count2 = 0
count3 = 0

_list1 = []
with open("list1.txt", "a+") as fp:
    for x in fp:
        _list1.append(x.rstrip())
    fp.close()

_list2 = []
with open("list2.txt", "a+") as fp:
    for x in fp:
        _list2.append(x.rstrip())
    fp.close()

_list3 = []
with open("list3.txt", "a+") as fp:
    for x in fp:
        _list3.append(x.rstrip())
    fp.close()

try: os.system("clear")
except: os.system("cls")

def ad1():
    global _list1, count1
    while True:
        try:
            _list1 = list(set(_list1))
            req = requests.get("https://www.roblox.com/user-sponsorship/1")
            req_img = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', req.text).group(1)
            req_text = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', req.text).group(2)
            count1+=1
            if req_img not in _list1:
                _list1.append(req_img)
                with open("list1.txt", "a") as list1_txt:
                    list1_txt.write(f"{req_img}\n")
                    list1_txt.close()
                print(f"Ads scraped! Ads Name: {req_text} | {req_img}", end="\n")
                embed = {
                    "content": None,
                    "embeds": [
                        {
                            "title": "New ad found!",
                            "description": f"**Name**: {req_text}",
                            "color": 2607871,
                            "image": {
                                "url": req_img
                            }
                        }
                    ]
                }
                requests.post(wh1, json=embed, headers={"Content-Type": "application/json"})
                time.sleep(wait)
                pass
            else: pass
        except: pass
        continue

def ad2():
    global _list2, count2
    while True:
        try:
            _list2 = list(set(_list2))
            req = requests.get("https://www.roblox.com/user-sponsorship/2")
            req_img = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', req.text).group(1)
            req_text = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', req.text).group(2)
            count2+=1
            if req_img not in _list2:
                _list2.append(req_img)
                with open("list2.txt", "a") as list2_txt:
                    list2_txt.write(f"{req_img}\n")
                    list2_txt.close()
                print(f"Ads scraped! Ads Name: {req_text} | {req_img}", end="\n")
                embed = {
                    "content": None,
                    "embeds": [
                        {
                            "title": "New ad found!",
                            "description": f"**Name**: {req_text}",
                            "color": 2607871,
                            "image": {
                                "url": req_img
                            }
                        }
                    ]
                }
                requests.post(wh2, json=embed, headers={"Content-Type": "application/json"})
                time.sleep(wait)
                pass
            else: pass
        except: pass
        continue

def ad3():
    global _list3, count3
    while True:
        try:
            _list3 = list(set(_list3))
            req = requests.get("https://www.roblox.com/user-sponsorship/3")
            req_img = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', req.text).group(1)
            req_text = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', req.text).group(2)
            count3+=1
            if req_img not in _list3:
                _list3.append(req_img)
                with open("list3.txt", "a") as list3_txt:
                    list3_txt.write(f"{req_img}\n")
                    list3_txt.close()
                print(f"Ads scraped! Ads Name: {req_text} | {req_img}", end="\n")
                embed = {
                    "content": None,
                    "embeds": [
                        {
                            "title": "New ad found!",
                            "description": f"**Name**: {req_text}",
                            "color": 2607871,
                            "image": {
                                "url": req_img
                            }
                        }
                    ]
                }
                requests.post(wh3, json=embed, headers={"Content-Type": "application/json"})
                time.sleep(wait)
                pass
            else: pass
        except: pass
        continue

for x in range(th):
    threading.Thread(target=ad1).start()
    threading.Thread(target=ad2).start()
    threading.Thread(target=ad3).start()

print("Scraper started!")
while True:
    print(f"{count1}, {count2}, {count3}\r", end="\r")