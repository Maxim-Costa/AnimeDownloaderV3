from bs4 import BeautifulSoup
import requests
import json
import os
import subprocess
import aria2p


def SibnetLink(url):
    html = requests.request("GET", url, headers={},
                            data={}).text.encode('utf8')

    soup = BeautifulSoup(html, "html.parser")
    step = soup.find_all("script")
    l = str(step[23])
    r = l.split("\"")
    return r[r.index("video/mp4")-2]



url = "https://vostfree.com/148-no-game-no-life-vostfr-ddl-streaming-1fichier-uptobox.html"
AnimeName = "No-Game-No-Life"


templateLink = {"Sibnet": "https://video.sibnet.ru/shell.php?videoid={id}",
                "Mytv": "https://www.myvi.tv/embed/{id}"}

html = requests.request("GET", url, headers={},
                        data={}).text.encode('utf8')
soup = BeautifulSoup(html, "html.parser")

step = soup.find_all("div", class_="button_box")
step1 = soup.find_all("div", class_="player_box")


DicoId = dict()
DicoAll = dict()
Link = dict()

Final = []
FinalId = dict()

for i in step1:
    DicoId[i.get("id")] = i.string

nbEpisode = len(step)
g = 0

for i in step:
    g += 1
    for j in i.contents:
        if not (j.string in DicoAll.keys()):
            DicoAll[j.string] = {}
        DicoAll[j.string][g] = DicoId["content_"+j.get('id')]

for k, v in DicoAll.items():
    print(f"{k} : {len(v.keys())}/{nbEpisode}")
    if len(v.keys()) == nbEpisode:
        if k in templateLink:
            for k1, v1 in DicoAll[k].items():
                Link[k1] = templateLink[k].replace("{id}", v1)
                FinalId[k1] = v1
        else:
            print(f"{k} not in template")

print("\n")

for k, v in Link.items():
    print(f"{k} : {v}")
    getVersion = subprocess.Popen(
        './cusi.sh '+v, shell=True, stdout=subprocess.PIPE).stdout
    version = getVersion.read()
    version = version.decode()
    Final.append(version.rstrip())

print("\n")

choix = int(input(" Voulez vous continuez OUI=1/NON=0 >>"))

if choix == 0:
    exit()
else:
    os.system("mkdir /media/CDisk_share/Anime/"+AnimeName)

    with open("/media/CDisk_share/Anime/"+AnimeName+"/anime.json","w+") as fp:
        json.dump(FinalId, fp)

    # initialization, these are the default values
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://localhost",
            port=6800,
            secret="5Uj3I+RPGwZI++qmXVOAf7J57Jh2xOasZgpR807TV7Y="
        )
    )

    for i in Final:
        if i != "":
            downloads = aria2.add_uris(i, dict(dir="/media/CDisk_share/Anime/"+AnimeName))
        else:
            print("error link")
