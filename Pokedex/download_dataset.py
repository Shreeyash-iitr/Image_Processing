from bs4 import BeautifulSoup
import argparse
import requests

#========  Argument parser from commands =================
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pokemonlist",required=True)
ap.add_argument("-s","--sprites", required=True)
args = vars(ap.parse_args())
#print(args)

#========== Extracting pokemon names from html file==========
soup = BeautifulSoup(open(args["pokemonlist"]).read())
names = []
for link in soup.findAll("a"):
    names.append(link.text)
#print(names)

#========== changing names ============
for name in names:
    parsedName = name.lower()
    parsedName = parsedName.replace("'","")
    parsedName = parsedName.replace(". ", "-")
    if name.find(u'\u2640')!= -1:
        parsedName = "nidoran-f"
    elif name.find(u'\u2642') != -1:
        parsedName = "nidoran-m"
#==========downloading and saving file===========
    print("[x] downloading %s"% (name))
    url = "http://img.pokemondb.net/sprites/red-blue/normal/%s.png"%(parsedName)
    r = requests.get(url)
    if r.status_code != 200:
        print("[x] error downloading %s"%(name))
        continue
    f = open("%s/%s.png"%(args["sprites"],name.lower()), "wb")
    f.write(r.content)
    f.close()
    #print(url)

#python /home/shreeyash/PycharmProjects/untitled/Pokedex/code.py --pokemonlist pokemon_list.html --sprites sprites

