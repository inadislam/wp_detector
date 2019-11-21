import requests
import os

o = open ("others.txt", "a+")
wp = open ("wp.txt", 'a+')
wl = open ("list.txt").read().split("\n")

class tcolor:
    yellow = '\33[33m'
    red = '\33[31m'
    green = '\33[32m'

def splitter(host):
        host = host
        print (tcolor.green+"[START] "+tcolor.yellow+"Scanner Started Successfully")
        
        try:
            test_response = requests.get(host+'/').text
        except requests.exceptions.HTTPError:
            o.write(host+'#notWP\n')
            print (tcolor.red+"[ERROR] "+tcolor.yellow+"Connection Error")
            pass
        except requests.exceptions.ConnectionError:
            o.write(host+'#notWP\n')
            print(tcolor.red+"[ERROR] "+tcolor.yellow+"Connection Error")
            pass
        else:
            if "wp-content" in test_response:
                wp.write(host+'\n')
                print(tcolor.yellow+"[OK] "+tcolor.green+"It is a Wordpress Site")
            else:
                o.write(host+'#NotWP\n')
                print(tcolor.yellow+"[ERROR] "+tcolor.red+"It is not a Wordpress Site")

def banner():
    os.system("clear")
    
    print("###########################################################")
    print("#        Tool: WordPress Site Detector                    #")
    print("#        Author: Inad Islam                               #")
    print("#   A Wordpress site detector			     #")
    print("###########################################################")

def s():
    banner()
    for item in wl:
        if (item == ""):
            continue
        splitter(item)

s()
