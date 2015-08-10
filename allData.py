__author__ = 'zeyneptekiner'
import json
import urllib
import os

sayi = ["75", "150", "225"]
adres = ["glance", "keystone", "ceilometer", "cinder", "trove", "sahara"]
for i in adres:

    url = "https://bugs.launchpad.net/"+i+"/+bugs/++model++?orderby=importance&start=0"
    if url == "https://bugs.launchpad.net/"+i+"/+bugs/++model++?orderby=importance&start=0":
        response = urllib.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))

        for a in sayi:
            url = "https://bugs.launchpad.net/"+i+"/+bugs/++model++?memo"+a+"=&orderby=importance&memo="+a+"&start="+a+""
            response = urllib.urlopen(url)
            data = json.loads(response.read().decode("utf-8"))


            items = data["mustache_model"]["items"]
            f = open('allData.txt', 'w')

            for item in items:
                if item["importance"] == "Critical" :
                    line = item["status"] + " " + item["importance"] + " " + item["age"] +" " + item["last_updated"] + " " + item["title"] + " " + item["bug_url"]
                    print line
                    f.write(line)
                    f.write("\n")
f.close()

