import hashlib
from keyauth import *
from console import Console
import os
import json
import sys
vanity = '/fastboosts'
config = json.load(open("license.json", encoding="utf-8"))
log = Console()
def cls():
    os.system('cls' if os.name =='nt' else 'clear')
def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "Sonicboostsss's Application", # App name 
    ownerid = "71CaWoXYWE", # Account ID
    version = "1.0", # Application version. Used for automatic downloads see video here https://www.youtube.com/watch?v=kW195PLCBKs
    hash_to_check = getchecksum()
)

cls()

if keyauthapp.checkblacklist():
    log.error("You are blacklisted from our system." )
    quit()
    
def validate():
    if keyauthapp.license(config["license_key"]):
        quit()
    else:
        log.success("Successfully Logged Into : ", vanity)
        time.sleep(2)
        os.system('cls')
        

def answer():
    try:
        key = input("""License Key: """)
        x = {"license_key": key}
        config.update(x)
        json.dump(config, open("config.json", "w"), indent = 4)

    except KeyboardInterrupt:
        os._exit(1)

if "license_key" not in str(config):
    answer()

