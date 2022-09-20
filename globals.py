# MathClav v0.5  
# by : Team SchnakyX & apparentés (TS&a)
#
# Licence (CC BY-NC-SA 4.0) 2022 - MathClav
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/4.0/ 
# or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
#
# This program is distributed in the hope that it will be useful,
# for any question, please contact us at paul.giroux87@gmail.com

import os

def initialize():
    global whith,bg,bgMath,bgMath_white,bg_buton,bg_white,blue,red,green,red_dark,green_dark,data_path
    whith = '#f0f0f0'
    bg = '#1e1e1e'
    bgMath = '#3A3A3A'
    bgMath_white = '#edf2fb'
    bg_buton = '#2e2e2e'
    bg_white = '#FFFFFF'
    blue = '#4188fd'
    red = '#ea4646'
    green = '#5cc25c'
    red_dark = '#ff7f7f'
    green_dark = '#7fff7f'

    data_path = os.path.expanduser('~')+"\AppData\Local\mathclav0_5"

    if not(os.path.exists(data_path)):
        os.makedirs(data_path)
        os.makedirs(data_path+"\historique")
        os.makedirs(data_path+"\log")
        os.makedirs(data_path+"\settings")

    # for user they alredy have download verssion 0.1 of MathClav
    if not(os.path.exists(data_path+"\settings")):
        os.makedirs(data_path+"\settings")