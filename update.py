
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
g.initialize()

def update_download(root):
    url = 'https://github.com/ppgg88/mathclav/raw/master/installeur/MathClav.exe'
    try:
        file = req.get(url, allow_redirects=True)
        open(g.data_path+'\install_new.exe', 'wb').write(file.content)
        #open('install_new.exe', 'wb').write(file.content)
    except:
        print("Erreur de téléchargement")
        return(-1)
    root.quiter()
    os.system(g.data_path+'\install_new.exe')
    os.system("unins000.exe")
    


import ctypes 
def update_q(root):
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    if g.v != verssion():
        if Mbox('Update', 'Une nouvelle verssion est disponible, voulez vous l\'instaler ?', 4) == 6:
            update_download(root)
    

if __name__ == '__main__':
    print(verssion())
    update_q(None)
    #update_download()