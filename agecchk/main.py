from console import Console
import tls_client 
import re
import os
import re
import bs4
from bs4 import BeautifulSoup
from threading import Lock
import  yaml
config = yaml.safe_load(open("config.yml"))
lock = Lock()
prxy = config['proxy']
proxyurl = f'http://{prxy}'
threads = config['threads']
from bs4 import BeautifulSoup
session = tls_client.Session(

    client_identifier="chrome_133",

    random_tls_extension_order=True

)
def calculate_time_passed(date_str):
     from datetime import datetime, timezone
     given_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
     current_time = datetime.now(timezone.utc)
    
     time_passed = current_time - given_date
     return time_passed
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
        return False
    
    line = lines[0].strip()
    with open(filename, "w") as file:
        file.writelines(lines[1:])
    
    parts = line.split(":", 2)
    if len(parts) < 2:
        return None, None 
    
    email, password = parts[0], parts[1]
    return email, password


class cookie_fetch:

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
        self.session = tls_client.Session(
        client_identifier="chrome_134",
        random_tls_extension_order=True,
        h2_settings={
            "HEADER_TABLE_SIZE": 65536,
            "MAX_CONCURRENT_STREAMS": 1000,
            "INITIAL_WINDOW_SIZE": 6291456,
            "MAX_HEADER_LIST_SIZE": 262144,
        },
        h2_settings_order=[
            "HEADER_TABLE_SIZE",
            "MAX_CONCURRENT_STREAMS",
            "INITIAL_WINDOW_SIZE",
            "MAX_HEADER_LIST_SIZE",
        ],
        supported_signature_algorithms=[
            "ECDSAWithP256AndSHA256",
            "PSSWithSHA256",
            "PKCS1WithSHA256",
            "ECDSAWithP384AndSHA384",
            "PSSWithSHA384",
            "PKCS1WithSHA384",
            "PSSWithSHA512",
            "PKCS1WithSHA512",
        ],
        supported_versions=["GREASE", "1.3", "1.2"],
        key_share_curves=["GREASE", "X25519"],
        cert_compression_algo="brotli",
        pseudo_header_order=[":method", ":authority", ":scheme", ":path"],
        connection_flow=15663105,
        header_order=["accept", "user-agent", "accept-encoding", "accept-language"],
    )
        self.sls = None
        self.email,self.password = process_account_file("input/accs.txt")

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
            with open('output/failed/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')
            return False
    def login_account(self):
        headers = {**self.BASE_HEADERS, 'x-xsrf-token': self.xsrf}
        json_data = {
    'email': self.email,
    'password': self.password,
 }
        import random
        max_retries = 7 
        retry_delay = [1,2,3]

        for attempt in range(max_retries):
            response = self.session.post(
                'https://api-id.streamlabs.com/v1/auth/login',
                headers=headers,
                json=json_data,
                proxy=proxyurl
            )
            
            if response.status_code == 200:
                break
            
            elif response.status_code == 422 and response.text.strip() == '{"message":"Our servers are having issues, please try again later."}':
                time.sleep(1)
                continue
            
            elif response.status_code == 401:
                log.error(f'Unauthorized: {self.email}:{self.password} - Retrying ({attempt+1}/{max_retries})')
                time.sleep(random.choice(retry_delay))
                continue
            
            else:
                with open('output/failed/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')
                break
        else:
            log.error(f'Login Failed , {black}Retries={reset}{Fore.LIGHTCYAN_EX}{max_retries}{reset} {black}Attempts={reset}{Fore.LIGHTYELLOW_EX}{self.email}{reset}:{Fore.LIGHTBLUE_EX}{self.password}{reset}')
            with open('output/failed/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')

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
        
        try:
            csrf = self.csrf(self.xsrf)
            
        except Exception as e:
            log.error(f'Failed to get CSRF token : {e}')
            with open('output/failed/failed.txt', 'a') as file:
                file.write(f'{self.email}:{self.password}\n')
            return False
        head = None
        cookies = None
        params = None
        if csrf:
            pomo = self.session.cookies.get('slsid')
            self.get_age(pomo=pomo,csrf=csrf)





    def get_age(self,pomo,csrf):
        headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://streamlabs.com/dashboard',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'X-CSRF-TOKEN': csrf,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"134.0.6998.89"',
    'sec-ch-ua-full-version-list': '"Chromium";v="134.0.6998.89", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.89"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
}
        cookies = {
    '__sla-uuid': '680dbf5d-536f-4ee5-8250-ee51917f8c2c',
    '_gcl_au': '1.1.1380004474.1742098453',
    'sl-impact-download': 'false',
    '_ga': 'GA1.1.1886588857.1742098456',
    'IR_gbd': 'streamlabs.com',
    'sa-user-id': 's%253A0-eed8ad83-2bb1-497e-78a2-d24d7b02631d.2wLRAP9%252BVJh4Y8r3jPNyb7ButejAKdI%252FhjPIXSvqgLo',
    'sa-user-id-v2': 's%253A7titgyuxSX54otJNewJjHQ.EDlHMCe12B0Q%252BjKPF43NnjuP5%252BQw4BohINyxOqrJSwM',
    'sa-user-id-v3': 's%253AAQAKIB80RWuWJ6lmh4RS6gkMyn12ONL5S5shnZ0T-BkfcnloEHwYAiCYoNm-BjoEydiQQkIEdXysUQ.%252BPIvejOzCk8MtoRrzYyjn5KB79IE6klsL5lOJWl%252BP84',
    '_pin_unauth': 'dWlkPVpqRXpOVEZtTkRJdFpqaGlOQzAwTWpSa0xUbG1NakF0WlRka00ySm1ZbUUyTkdZMg',
    'pa_31738_1_sb_shown': '1',
    '_fbp': 'fb.1.1742098492364.690358932492535678',
    'langCode': 'en-US',
    '__stripe_mid': '7369d383-e02e-4133-8531-df1afa59e60bc002fc',
    'cf_clearance': 'R6dsDuPpC.FWvdfPtxtQO.Sfm14yCN6_EDb6yLnyksw-1742098986-1.2.1.1-EhJ8GIaKO46rySDerVHEVM0aHq.93PruNo6m5BPdZObY4BLIwq49v5BVRKznqcKMzVI_W0zYk7bUp.ezGL1nVa6WBbqjXlCmf3Oq8OL9tuep2A1lejFRiNhSOjUtRXlpbaNghkh.nm2fdpFiHapvRBz9cK1uUuozoYq3d1lwozC.qNarxuCG26vwt6h0g0KAfAVcFyyk766hSLloHxYBtUBIPuVqf8VKzpAwZlCFNcdymiHyHe9STiOacofxfLyzV4LKP5j_UT4Gdo.kvt3MyBMzxwqiu4YdQ6ADVy2v6ypG2ZKBCfbfbBY1cEF2xK.goUl0nuELqIc5ccTevmLDjw8h12DcuSfVw_M58OiSomnFUb.GMezmRgOgNeQSPONIz6QRgI06LRkRD.G2Df3H8.n.fgv9C9RGb6YhUer8mYc',
    '__cf_bm': '6CEC90xZanH9fu5iEj9pphOXWP7CMNXKe8iAooKxxtM-1742104639-1.0.1.1-FRGfJoUd1NXAhOKDN0U78FM_FfBvyarD8y.BR1TrEO7iB3CUCvLPNpaF5bvVWT6.aN6G9zRfYRO._crN3JVlccj5jzf767.vN6tAYH1FfvU',
    '__stripe_sid': '57b85786-b7b9-4171-b7f5-c011d888978900964f',
    'IR_23134': '1742104665758%7C0%7C1742104665758%7C%7C',
    'IR_PI': '461c6b62-021d-11f0-98c3-91cab5fd5688%7C1742104665758',
    '_uetsid': '20d295a0021d11f0a0df99fb6393294f',
    '_uetvid': '20d2e530021d11f0aa124559a2c9dd7f',
    'ab_testing': 'eyJpdiI6IkNuc0lsUDliQWRyNkV3Uks2dndvWWc9PSIsInZhbHVlIjoiYjB2RmJoay9KRDhOMW1EaXJzcHVVSEpucWdrSG4xRDNRdjJhcm9xdVdadnFZcjJCWjRGR2NVbGRVejhqeldSZmp4ekJLeVc5dEloQU1aZTh6NU1SaHhYWXRqODZ6TTJoU2hWMTdSM3lLZGN1M211VVhZQW5WMkFZcXY2Tzdqc0RFME9rWXVaRkFOZ2NSUVUzYjdLMHhuNFRPa25kWVFzUEpXTnNBSW80RURUUUNsM1luakI4aHNmUk9XaDUvaVlKaGg2Ymp4K3NtRGlyNGJ6RTZ5cWNaQ3J6c0MyWXg1U3lvUmxpVmtMZU9FbU81MFZpWnpoZHA2QnAreS9IdmRSdWRXYVhwZXJzVW9nY2N2YlJMNEpIb09TdVp0UWZNdCt6TjQ5bzhKWEZEUXV0Z1lQSk9wblk1amZoZHZ3NEt5VjUxbDkwM0t4T1NPT3psUkY5cm0ydk9aSERRdXBZODNnMUtwMkhOQ2Y5QTEvSzJWQ04xdk11NlhkeXNKZWNrSm43YWErREFtZ3N3aGRpNzQ2N29mbW5hTTV2UHdBWnkrSW8rZ1R3WU1idDBNdDdLR1FKNWRMcnBOQUcrMlczOHNQSU5UOGx0dzRpK2lOQ0dxLzh0eHZFVVd5MW5kT2tNaHJiL3A5M3dEVmdaM1ArU3BnOTVIVlIrTHd0NzJGZHczTXE2di9LTzkxWm1NZ20zR3ZuU3c4bGh1RTdjWWhhZHdQVGdRYjZtb0R0MnAvZWZ0NGl5QU9KUFdRbUtuZTFBVHhpYzE4cXoxVkZIV1hyOVVjNHQ0LzhRYm5JOTdmYXM3OGF4aHJiQnJ0RlNubzlrNGVjNGg0ZDZoc3ZmSlFwc1ZyMkZSc2U3WUtFbE5LUndBQ0drWjd1VW9xWnB3Smo1L3A5WXNSK2VkVkpTOWhaN2oyRzVtZUFjdjRRbFBQUEhHcEVQOXBhRFgyTmV1WDVkK2VEYzB4OGlnQVJyeDVQZWZiczNSN05zU0l3Zzd3Y2dTZ0d1WXFwZXJLcS95NEVlbElQVXBPRUpXL3ZKWWZiTFlJaFpnMy82Z3htTDE0VG5QdTRta3gzZGVvaVhqcHh3OTh1dkR4d2duQWYyNC9meU5jZ0VIL2JwZm1aNms4eUpJNHFTWWtKeE9UOVRPWmozNUUyRkh4c0J0T0JiRTZYbU51Q1hoTzRlUkRTQnBVYWM5WndOb3VVSFJPQ05PK0RPSVlROVFnUkd0YURQSFdzcVVOZ21YdWRCZ3EybnlLc3piV09vVUZyZEt3Y1owTjRSM2lJZDFBcWM3ejdMWkdSUFNQNFdCeGsxS21UeXlOSTU2c0J1M2V1bzYxeFdlcUw3TCtDS2hEUnNuTjdyWnAvWm1zckRvQTJpZXhYRldBZW5GVzB5RFFyclk3aVBrTmMyck1YZmx5RWxGTzFPWlVSUGkvZSsyMjY3WHZIdER1bkUyNTIiLCJtYWMiOiI0Y2U3MGNmZTFlNDEyODk4Y2YyNTEyZDcxMjFkYzg1NTYwMjllMGFiNmVlOTFiYjQ4M2I1OGIzMTljZTk3YzE0IiwidGFnIjoiIn0%3D',
    '_rdt_uuid': '1742098455775.0de28f8c-f8ec-4626-8884-e9894f446663',
    '_ga_DXPRHH738Q': 'GS1.1.1742104649.2.1.1742104784.60.0.0',
    'XSRF-TOKEN': 'eyJpdiI6IlN6OWg0a0JGNGxhVkIrektDd2pFYVE9PSIsInZhbHVlIjoidGlKb0JQYUE3d0F5MXg1ZEV2dURXRVQxemM5M2NydVUwSjF0OFkremNndnFsblcwVzV5aDJ2UTdkTVlIZ0NhMyIsIm1hYyI6ImViMWE4NDNlMWIyNTFkOTZkMGRkZTFmYTA5ODA3MjUzNzQwY2NjYTc4ZTU3ZThjY2FmNzM5Njg4NTI4OGFkZGUiLCJ0YWciOiIifQ%3D%3D',
    'slsid': pomo,
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Mar+16+2025+11%3A29%3A44+GMT%2B0530+(India+Standard+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=03bc9737-1660-4848-8ec3-bff80e771084&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
}
        params = {
    'location': 'dashboard',
}
        import random
        max_retries = 5
        retry_delay = [1,2,3]

        for attempt in range(max_retries):
            response = self.session.get(
                'https://streamlabs.com/api/v5/user/notifications',
                params=params,
                headers=headers,
                cookies=cookies,
                proxy=proxyurl
            )
            if response.status_code == 200:
                date = response.json()['notifications']['list'][-1]['created_at']
                time_passed = calculate_time_passed(date_str=date)
                self.save_time_passed(time_passed)
                days = time_passed.days
                hrs = time_passed.seconds // 3600
                dayte = f'{days} Days {hrs} Hours'
                log.success(f'Logged in: {b}email:{r}{Fore.LIGHTGREEN_EX}{self.email}{r}, {b}password:{r}{Fore.LIGHTCYAN_EX}{self.password}{r}, {b}Age:{r} ', dayte)
                break
            
            elif response.status_code == 422 and response.text.strip() == '{"message":"Our servers are having issues, please try again later."}':
                time.sleep(1)
                continue
            
            elif response.status_code == 401:
                log.error(f'Unauthorized: {self.email}:{self.password} - Retrying ({attempt+1}/{max_retries})')
                time.sleep(random.choice(retry_delay))
                continue
            
            else:
                with open('output/failed/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')
                break
        else:
            log.error(f'Login Failed , {black}Retries={reset}{Fore.LIGHTCYAN_EX}{max_retries}{reset} {black}Attemps={reset}{Fore.LIGHTMAGENTA_EX}{self.email}{reset}:{Fore.LIGHTWHITE_EX}{self.password}{reset}')
            with open('output/failed/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')


            


    def save_time_passed(self,time_passed):
     days = time_passed.days
     hours = time_passed.seconds // 3600

     if days == 0:
        filename = f"output/unpullable/0_days_{hours}hrs.txt"
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                file.write(f"{self.email}:{self.password}\n")
        else:
            with open(filename, "a") as file:
                file.write(f"{self.email}:{self.password}\n")
     else:
        with open("output/pullable/claimable.txt", "a") as file:
            file.write(f"{self.email}:{self.password}\n")
    def csrf(self, xsrf):
        url = "https://api-id.streamlabs.com/v1/identity/clients/419049641753968640/oauth2"
        payload = {
            "origin": "https://streamlabs.com",
            "intent": "connect",
            "state": ""
        }
        headers = {
            "X-XSRF-Token": xsrf,
            "Content-Type": "application/json"
        }

        response = self.session.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            redirect_url = data.get("redirect_url")
            
            if redirect_url:
                while redirect_url:
                    redirect_response = self.session.get(redirect_url, allow_redirects=False)
                    
                    self.session.cookies.update(redirect_response.cookies)
                    if redirect_response.status_code in (301, 302) and 'Location' in redirect_response.headers:
                        redirect_url = redirect_response.headers['Location']
                    else:
                        match = re.search(r"var\s+redirectUrl\s*=\s*'(.*?)';", redirect_response.text)
                        if match:
                            redirect_url = match.group(1)
                            red4 = self.session.get(redirect_url)
                            self.session.cookies.update(red4.cookies)
                            red5 = self.session.get("https://streamlabs.com/dashboard")
                            self.session.cookies.update(red5.cookies)
                            soup = BeautifulSoup(red5.text, "html.parser")
                            csrf = soup.find("meta", {"name": "csrf-token"})["content"]
                            return csrf

            else:
                log.error("Redirect URL not found in the response.")
                return None
        else:
            log.error(f"Request failed: {b}{response.status_code}{r} - {b}{response.text}{r}")
            with open('output/failed/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')
            return None
        



    
def create_accounts(num):
    threads = []
    for _ in range(num):
        creator = cookie_fetch()
        thread = threading.Thread(target=creator.run)
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
while True:
 if __name__ == "__main__":
    create_accounts(threads) 

                    

                                       
        

 




    
            
            