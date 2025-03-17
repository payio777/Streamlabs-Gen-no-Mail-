from validate import validate
#validate()

from console import Console
import tls_client 
from threading import Lock
import  yaml
config = yaml.safe_load(open("config.yml"))
lock = Lock()
proxyurl = config['proxy']
threads = config['threads']
import string
import random
session = tls_client.Session(client_identifier="chrome_133",random_tls_extension_order=True)
import threading
def remove_content(filename, delete_line: str) -> None:
        with lock:
            with open(filename, "r+") as io:
                content = io.readlines()
                io.seek(0)
                for line in content:
                    if not (delete_line in line):
                        io.write(line)
                io.truncate()
from colorama import Fore
import time
black = Fore.LIGHTBLACK_EX
reset = Fore.RESET
log = Console()
from colorama import Fore

b = Fore.LIGHTBLACK_EX
r = Fore.RESET

def get_second_slsid(session):
    slsid_cookies = [cookie.value for cookie in session.cookies if cookie.name == "slsid"]
    
    if len(slsid_cookies) >= 2:
        return slsid_cookies[1]
    else:
        return None
    
def process_account_file(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    if not lines:
        log.info('No Accounts To Process')
        exit()
    
    line = lines[0].strip()
    with open(filename, "w") as file:
        file.writelines(lines[1:])
    
    parts = line.split(":", 2)
    if len(parts) < 2:
        return None, None 
    
    email, password = parts[0], parts[1]
    return email, password

class Passchanger:

    file_lock = threading.Lock()
    promo_lock = threading.Lock()
    acc_lock = threading.Lock()
    
    BASE_HEADERS = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'client-id': '419049641753968640',
        'content-type': 'application/json',
        'origin': 'https://streamlabs.com',
        'priority': 'u=1, i',
        'referer': 'https://streamlabs.com/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    def __init__(self):
        self.session = tls_client.Session(client_identifier="chrome_133",random_tls_extension_order=True)
        self.sls = None
        self.email,self.password = process_account_file("input/accs.txt")
        self.newpass = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))

        self.promo = None
    # u can use a xsrf fetcher too but is that important ? fucking no , Will one work ?  Fuking yes Dont't Q me for this 
        self.xsrf =  'eyJpdiI6InVqZlVJNk5xMEVLRDM1SGhEV3BlRXc9PSIsInZhbHVlIjoiNUw2eFBGVDA2dTRZUENtUU5KZDdQWDAzc210RlRXNWl0NlRSYXJjQTBTMHBuWjRZZXZMN2pKZTRHU20xUEQ2aSIsIm1hYyI6Ijg4MGFhZDE1ZGFkZTNlMTA5MWM3ZmExODc4Y2M5YjRjZDA4YTM0M2U2ZjM5NDhmN2Q1MGU1MDFiNzc3NjIyZmEiLCJ0YWciOiIifQ=='
    def run(self):
        try:

            if not self.login_account():
                return False
                   
            return True
            
        except Exception as e:
            log.error(f"Thread failed: {str(e)}")
            return False
    def login_account(self):
        headers = {**self.BASE_HEADERS, 'x-xsrf-token': self.xsrf}
        json_data = {
    'email': self.email,
    'password': self.password,
 }
        cookies = {
    '_gcl_au': '1.1.577199988.1740492535',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Feb+25+2025+19%3A38%3A55+GMT%2B0530+(India+Standard+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ae102e0a-c9de-4231-af28-3aacc1110706&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fstreamlabs.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
    '_rdt_uuid': '1740492536565.ec05129a-8bb7-487f-8a7e-b95c25935c78',
    '_ga': 'GA1.1.617127087.1740492537',
    'IR_gbd': 'streamlabs.com',
    'IR_23134': '1740492537088%7C0%7C1740492537088%7C%7C',
    'pa_31738_1_sb_shown': '1',
    '_uetsid': '0e1dc940f38211ef9d316ffa56f03cc2',
    '_uetvid': '0e1e13c0f38211ef9dfec3e07238a0f2',
    '_pin_unauth': 'dWlkPU0yTTVZVEF5T1RndE1qUTNaUzAwT0RjeUxUazJZVGN0TlRFek56TmhNREk0TmpobA',
    'pushalert_31738_1_subs_status': 'canceled',
    '_fbp': 'fb.1.1740495998931.151017517909302227',
    'XSRF-TOKEN': 'eyJpdiI6InFQNk1sNkZ1bThtYkNhbnQyenZwYUE9PSIsInZhbHVlIjoiS3RLcFNSdEYxMzZFL01XTGFwU2V2eU9SNE5qMGJSMlgxWk1JcE5yblppY1FxYWZNRW5zb0g2U1RyZk5mL3h3dSIsIm1hYyI6ImRhZTY5YjViOGYzZGJiYTU2NmYyOWU3OTlhMmE4ZDJmNzg4MzAxNDljZGUxM2ViNjU3ZDZlMmI2MzljODE5N2YiLCJ0YWciOiIifQ%3D%3D',
    'slsid': 'eyJpdiI6ImRTTXBOSm9QK0FiTkVSNWl5MXhydFE9PSIsInZhbHVlIjoiS1p5ZnA2YmZNNFQrNXg3YUZnaFlUTzN3OFNhYTZOVmh3a3k0S21kc1VjN1R2SmtTNHlSaUtOQXp4WHFkUWpOUyIsIm1hYyI6IjRhNjg1NGQ0YTk2ZTRjMWI5MDM4NWM4OTkzZGM5OWVjNGY5MmNmOTZiMDRiY2EwMmE4MDAxNWIwZDFkYWVlYzMiLCJ0YWciOiIifQ%3D%3D',
    '__cf_bm': 'ipab0A29tN3BTIE5KJPZ96s6KRDVP9FQ0.iex0SVThg-1740495999-1.0.1.1-aS_LmVX.0g97CE9yzcutFDpONCi94ziw7FiKAtDbTouPnboviFs1oJcDoV54DkEk5wrwmlFMCDNnnlZOgCNwXA',
    '_ga_DXPRHH738Q': 'GS1.1.1740492536.1.1.1740496079.44.0.0',
 }

        response = self.session.post(
            'https://api-id.streamlabs.com/v1/auth/login',
            cookies=cookies,
            headers=headers,
            json=json_data,proxy=proxyurl
        )
        if response.status_code == 200:
            log.success(f'Logged Into : {b}email:{r}{Fore.LIGHTGREEN_EX}{self.email}{r}, {b}password:{r}{Fore.LIGHTMAGENTA_EX}{self.password}{r} ')
            access_token = response.cookies.get('access_token')
        else:
            log.error(f'Invalid Credentials: {b}email: {r}{self.email}{b}password: {r}{self.password}',response.status_code)
            with open('output/failed/login_failed.txt', 'a') as file:
                file.write(f'{self.email}:{self.password}\n')
            return False

        self.session.headers = {
        'accept'            : 'application/json, text/plain, */*',
        'accept-language'   : 'en-US,en;q=0.9',
        'cache-control'     : 'no-cache',
        'client-id'         : '419049641753968640',
        'content-type'      : 'application/json',
        'origin'            : 'https://streamlabs.com',
        'pragma'            : 'no-cache',
        'priority'          : 'u=1, i',
        'referer'           : 'https://streamlabs.com/',
        'sec-ch-ua'         : '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile'  : '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest'    : 'empty',
        'sec-fetch-mode'    : 'cors',
        'sec-fetch-site'    : 'same-site',
        'user-agent'        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-xsrf-token'      :  self.xsrf,
      }
        



        sookies = {
    'cf_clearance': 'aOxfki7B9.3_7z5LRvJ68gWNwTTXiZ2JAWu7QLy3Fis-1740753273-1.2.1.1-wBr9P6BtZS6q65rXtEEsIJF78OC93EG88x4SuFf7aYEgAvbveocbV_C2qM.BJ5XRElDVc8dZrIVTOKXTl0.1ov3Ex6uOnnsotLwqFI42CkjhwuWsYX2WXNH45f.yumPUlHFZ0vHrePdIa_XwPJLTnlkauMBULxeCq3emnFECHW9jjVgfr12sqzjxN9h3u3TkjsK0VL6t8vSfhA.pFKyRDaSK9a791RrZgQR3T6.eG0CeKj.0VqlvbQn6z3eaWWz.1uXv5H97P88gajlzN481Y3SNkdf_6grSZB.Pk_xX6u3kSo4_On8mdUTIjrdbQx9VPP2V8h9gZJnetzqyvye.Ue6lp__5bQj6Ty9NKZ7PPSgKSKDuIwIqzVws0zQFdR5S0RNsJdEvYlp9.2mr5Q6ldBk0fcvnOnV3saAvsElgfYppelor4ZY363oVmQ2LP3hfPN_SbbLlcPePM5YaLZXCWw',
    'sl-ab-t': 'A',
    '_gcl_au': '1.1.1084115903.1740753279',
    '_ga': 'GA1.1.74664961.1740753281',
    'IR_gbd': 'streamlabs.com',
    '_pin_unauth': 'dWlkPU0yUmtOekF3WkRndE56Sm1PQzAwWWpBM0xXSmtaR010TkdNNE4yTXlZVE00TUdObQ',
    'pa_31738_1_sb_shown': '1',
    '_fbp': 'fb.1.1740753340925.445480105445706577',
    '__stripe_mid': '4311fb7d-3e1d-4400-b528-488125746e1438b189',
    '__cf_bm': 'nECuJNZGKnaGL6keYIwwTnR06Axs_MptG2iIdS_tPoo-1741277392-1.0.1.1-k5azJn2Q6SPQgUzAtT2Kth_FbQzTm4dEk1hGuOIMwR3q1bf18riIFPzB10KCqjFTFMmeP8LsOOvaeKMfRxnp8u1MceMbDntDFgj7VOSvHHQ',
    'access_token': access_token,
    'streamlabs_id_session': 'RjshZFCJCMdTMSJBzuWJF6difkr5bsOWdf21UyZ2',
    'ab_testing': 'eyJpdiI6InQ0bXpCc3RYcGdwZnNsZ1ZTNjcvOEE9PSIsInZhbHVlIjoiMFJZR044ZnI1TFNMak9MWUJUNlBLRmFkNGVNZXRNUjdTUGZ3SmpCVWpGSDJUaW9NaWVCekllbWZId04zR1RLY3lNcWc3d2k1RWszMVYwMWwwZzQ5VW9wQXBHclp1R3ZkOHlXOGtKSFBsVlBmcWM4b0xBOWxHRkdHMlVZUmg0R3E5NGFqeVA1amV0clBobi9wZDVTd3o4M1lTU1kvT1ArbWtEd3dqcldQR3lLL3R5TDRRNGVFREprcm5wK3VJbURjVWd3d2dQS2kxdllTY2VxOGhCV3F3T0UvKzl4YzM2NVY1WWFwY3ZTQ1ZoWGg5a2djWHpQa2E2ZS9YbEQrcmg3YXBER0dobUdxUzZSbldCY0lSSlVUR2s1T0lnUVFjK1BOOW1LbGY4U3hvSGtCa0JSWkJtRnZOYktMTDJxVCtqcUxQeWdobUcxQ2tIRnl0M2VhYm0yWTAxQU5Qb0RhNFJvbmRhc3FnSjhRZlpxMmhFSXVKbHFnVTBCVW5ONEF3bElaQ1VuNUFuaUxtRUs5Vnh3NExjdjVobGRhZ3lER1U1cElqMlRWU0JGOXhQRnNPNXhSMWkvQ1FsWGt1amt4QkJoZUhHV2VtTkY4dHJiOFkyNTZSU0ZXRmpUOEJnQ2pGRFVGNlJicXFWeXVQY0FCNHBrZW5raEhuRGxkRkZFNUQ5bHBGVitycWJYU0JLZ2g0am9oZW5pbnZHaTVzb2FXY1dvdGx2UjFTTnBRTStxSW54Vkh6QjlVME5mYTNRVkZrdEloUTVZei80a2pXN3puOXdKMkY3ZHR6UUNab2tES2pqUXZ3UHpBOXUwaTcvZWUrakFvLzlUK0FyWjV2TkVhUmt4WDBIRVdWZ1JDSWthN2RNZ1JUaFVIYVJ6c1k1TXBJa0Qvb3RRL05aQWh5cjVKYmxOQnJsOHJuOVZIRnB3RzFtZ1laOXpBemk4NHNiazkydFhxM1dvMFJEdUlWQ1l1U3A0ZXYzSXFneE1ZRklBemY2TGo0NjAyQkxWUW5xSS9xb2MyUlNwc3QrVzFuUXVNMXlud3dIMEVuc3RUUmE5NS9zOG9lcWxWeUxlZXpxU2lWem1BeGdCYzVKaFNxYVVHNkJPMG9LVENMSFphWDIyOVczT1AySnBOc09IamN0REhtcW5pMGtzd1dtNHVOaTdETlorN0lucm53Nys2b2tMMGlMdDgiLCJtYWMiOiJhODE2NmUzZjZmMTI1YWM0NzRlZTlmZTdkOWRkMTE0ZWFiZDA5MWE0NjVmOWU3YjliMmE0MTJhMTYyY2QxYzJlIiwidGFnIjoiIn0%3D',
    'XSRF-TOKEN': 'eyJpdiI6ImNzczhtYUhqamZOdXV0Y2NCWU9KT3c9PSIsInZhbHVlIjoiVndPamNJSHFpWEp4STVDMnJlbTZGODE2Tnk1Ykd3QWI1UFpUOU1HQ0xyaVVlOGRwVXRsSlVaN2FPNm9SRGlVdSIsIm1hYyI6IjdiMTlkZDQ5MzIyYzUyM2Y3MTZlY2IyNmE3Njc5OTVjN2EyNjg5NmU4MmM0NWI1ZTM3MTY3MTA2ZDMxYjZjZDYiLCJ0YWciOiIifQ%3D%3D',
    'slsid': 'eyJpdiI6Imp5NmZrZmNka2dZcHIrcE1tMzE3K1E9PSIsInZhbHVlIjoiZTIwenRBZWN5cXRYT1NLM052a05CVG9JY010Uk9sc0VwTkgxQVQxOEhwVy9WVEp0SllhSHdPejRqUWhMQXpuTCIsIm1hYyI6IjNmNWNiYzA0YTkwMzZjMzlmMDM5MGE0ZmE5YTk0OWNkMzg5Y2JjMTE3ZmE5YjY4OTViYTdlZmFkNTBlNTMzNmYiLCJ0YWciOiIifQ%3D%3D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Mar+06+2025+21%3A50%3A49+GMT%2B0530+(India+Standard+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=7558cd94-16e5-489f-9264-ec01c50eb4ac&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    '_rdt_uuid': '1740753281013.a6b74ee6-77ac-4ea1-8699-e70733529ea1',
    'IR_23134': '1741278049673%7C0%7C1741278049673%7C%7C',
    '_ga_DXPRHH738Q': 'GS1.1.1741277399.2.1.1741278050.60.0.0',
    'IR_PI': '5519b719-f5e1-11ef-b1c4-d9b5262c89d3%7C1741278049673',
    '_uetsid': '75ad8ac0faa511efb29119272d687eea',
    '_uetvid': '2562e3a0f5e111efb6b6e16aa4fdce03',
           }
        snipe = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://id.streamlabs.com',
    'Referer': 'https://id.streamlabs.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': 'eyJpdiI6ImNzczhtYUhqamZOdXV0Y2NCWU9KT3c9PSIsInZhbHVlIjoiVndPamNJSHFpWEp4STVDMnJlbTZGODE2Tnk1Ykd3QWI1UFpUOU1HQ0xyaVVlOGRwVXRsSlVaN2FPNm9SRGlVdSIsIm1hYyI6IjdiMTlkZDQ5MzIyYzUyM2Y3MTZlY2IyNmE3Njc5OTVjN2EyNjg5NmU4MmM0NWI1ZTM3MTY3MTA2ZDMxYjZjZDYiLCJ0YWciOiIifQ==',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
          }
        
        json_data = {
    'current_password': self.password,
    'new_password': self.newpass,
    'new_password_confirmation': self.newpass,
           }
        response = self.session.post('https://api-id.streamlabs.com/v1/auth/change-password', cookies=sookies, headers=snipe, json=json_data,proxy=proxyurl)
        if response.status_code == 204:
            log.success(f'CHANGED :{black}old={reset}{Fore.LIGHTCYAN_EX}{self.password}{reset}, {black}New={reset}{Fore.LIGHTBLUE_EX}{self.newpass}{reset}:', self.email)
            with open('output/success.txt', 'a') as file:
                file.write(f'{self.email}:{self.newpass}\n')

        if response.status_code == 422:
            log.info('Wrong Pass',self.email)
            with open('output/failed/wrong.txt', 'a') as file:
                file.write(f'{self.email}:{self.password}\n')

        if response.status_code == 401:
            log.info(f'Invalid Creds {black}email={reset}{self.email}, {black}pass={reset}{self.password}')
            with open('output/failed/failed.txt', 'a') as file:
                file.write(f'{self.email}:{self.password}\n')


def create_accounts(num):
    threads = []
    for _ in range(num):
        creator = Passchanger()
        thread = threading.Thread(target=creator.run)
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

while True:
 if __name__ == "__main__":
    create_accounts(threads) 

                    

                                       
        

 




    
            
            