
import re, json, requests

def verssion():
    try:
        url = 'https://raw.githubusercontent.com/ppgg88/mathclav/master/verssion.json'
        resp = requests.get(url)
        data = json.loads(resp.text)
        return(data['verssion'])
    except :
        return("0")

import requests as req
import os
import globals as g
def update_download():
    url = 'https://github.com/ppgg88/mathclav/raw/master/installeur/MathClav.exe'
    try:
        file = req.get(url, allow_redirects=True)
        open(g.data_path+'\install_new.exe', 'wb').write(file.content)
    except:
        print("Erreur de téléchargement")
        return(-1)
    os.system('install_new.exe')
    os.system("unins000.exe")
    


if __name__ == '__main__':
    print(verssion())
    update_download()