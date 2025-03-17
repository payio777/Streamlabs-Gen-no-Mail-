from validate import validate

#validate()

from console import Console
import tls_client 
import re
from urllib.parse import unquote
from bs4 import BeautifulSoup
from threading import Lock
import  yaml
config = yaml.safe_load(open("config.yml"))
lock = Lock()
proxyurl = config['proxy']
threads = config['threads']
from bs4 import BeautifulSoup
session = tls_client.Session(

    client_identifier="chrome_133",

    random_tls_extension_order=True

)
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

class StreamlabsAccountCreator:

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
            with open('output/failed.txt','a') as file:
                file.write(f'{self.email}:{self.password}\n')
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
        import random
        max_retries = 5
        retry_delay = [1,2,3]

        for attempt in range(max_retries):
            response = self.session.post(
                'https://api-id.streamlabs.com/v1/auth/login',
                headers=headers,
                json=json_data,
                proxy=proxyurl
            )
            
            if response.status_code == 200:
                log.success(f'Logged Into : {b}email:{r}{Fore.LIGHTGREEN_EX}{self.email}{r}, {b}password:{r}{Fore.LIGHTMAGENTA_EX}{self.password}{r} ')
                break
            
            elif response.status_code == 422 and response.text.strip() == '{"message":"Our servers are having issues, please try again later."}':
                time.sleep(1)
                continue
            
            elif response.status_code == 401:
                log.error(f'Unauthorized: {self.email}:{self.password} - Retrying ({attempt+1}/{max_retries})')
                time.sleep(random.choice(retry_delay))
                continue
            
            else:
                with open('output/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')
                break
        else:
            log.error(f'Failed after {max_retries} attempts: {self.email}:{self.password}')
            with open('output/failed.txt', 'a') as file:
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
        
        try:
            csrf = self.csrf(self.xsrf)
            
        except Exception as e:
            log.error(f'Failed to get CSRF token : {e}')
            return False
        
        if csrf:
            cookies = self.session.cookies
            self.sls = get_second_slsid(self.session)
            cookie = f'slsid={self.sls}'
            headerss = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://streamlabs.com/dashboard',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-csrf-token': csrf,
    'x-requested-with': 'XMLHttpRequest',
}
            
            check_response = self.session.get('https://streamlabs.com/api/v5/user/accounts/settings-info', headers=headerss)
            platform = check_response.json()["platform_page_urls"]
            if platform == []:
                twitter_token = self.get_twitter_token()
                if twitter_token:
                
                    merge = self.merge(csrf=csrf, twitter_token=twitter_token)
                    if merge:

                       log.info(f'Merged Successfully {b}Token:{r}',f'{twitter_token[:20]}******')
                       with open('output/success.txt', 'a') as file:
                        file.write(f'{self.email}:{self.password}\n')
                       return False

                
            else:
                log.info(f'Already Linked {b}Email={r} {Fore.LIGHTBLUE_EX}{self.email}{reset}')
                with open('output/already_linked.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')

        else:
            #log.error('Failed to get CSRF token')
            with open('output/failed.txt', 'a') as file:
                file.write(f'{self.email}:{self.password}\n')
            return False
                

    def get_twitter_token(self):
        try:
            with open('data/tokens.txt', 'r') as f:
                tokens = f.readlines()
            if not tokens:
                log.error("No Twitter tokens found in tokens.txt.")
                return None
            token = tokens[0].strip()
            if ':' in token:
                token = token.split(':')[-1]
            with open('data/tokens.txt', 'w') as f:
                f.writelines(tokens[1:])
            return token
        except FileNotFoundError:
            log.error("tokens.txt file not found.")
            return 

    def merge(self,csrf,twitter_token: str) -> bool:
        try:
            response = self.session.get(
                    "https://streamlabs.com/api/v5/user/accounts/merge/twitter_account",
                    params={"r": "/dashboard#/settings/account-settings/platforms"}
                )
                
            if response.status_code != 200:
                log.error(f"Failed to get OAuth URL: {response.status_code}")
                return False
                    
            oauth_url = response.json().get('redirect_url')
            oauth_token = oauth_url.split("oauth_token=")[1]

            client = tls_client.Session('chrome_131', random_tls_extension_order=True)

            auth_response = client.get(
                    oauth_url, 
                    headers={'cookie': f"auth_token={twitter_token};"}
                )
                
            try:
                authenticity_token = auth_response.text.split(' <input name="authenticity_token" type="hidden" value="')[1].split('">')[0]
            except IndexError:
                twitter_tokenn = self.get_twitter_token()
                log.error("Invalid acc | RETRYING")
                remove_content(filename='data/tokens.txt', delete_line=twitter_token)
                return self.merge(csrf, twitter_tokenn)
                
            auth_data = {
                    'authenticity_token': authenticity_token,
                    'oauth_token': oauth_token
                }
                
            final_response = client.post('https://twitter.com/oauth/authorize', data=auth_data, headers={'cookie': f"auth_token={twitter_token};"})
            try:
                redirect_url = final_response.text.split('<p>If your browser doesn\'t redirect you please <a class="maintain-context" href="')[1].split('">')[0]
                    
                if redirect_url:
                    if 'You are being' in redirect_url:
                        print("Twitter account already used.")
                        
                        return False
                    client.headers.update({'referer': "https://twitter.com"})
                    response = self.session.get(unquote(redirect_url).replace("amp;", '').replace("amp;", ''))
                    if response.status_code == 302:
                        return True
                    else:
                        remove_content(filename='data/tokens.txt', delete_line=twitter_token)
                        print(f"Failed to link Twitter account: {response.status_code}")
                else:
                    remove_content(filename='data/tokens.txt', delete_line=twitter_token)
                    print("Failed to find redirect URL")
                    
                return False
            except IndexError:
                remove_content(filename='data/tokens.txt', delete_line=twitter_token)
                twitter_tokenn = self.get_twitter_token()
                log.error("Failed to extract redirect URL. retrying...")
                return self.merge(csrf, twitter_tokenn)
                    
        except Exception as e:
            print(f"Failed to link Twitter account: {e}")
            return False
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
            with open('output/failed.txt', 'a') as file:
                    file.write(f'{self.email}:{self.password}\n')
            return None
        



    
def create_accounts(num):
    threads = []
    for _ in range(num):
        creator = StreamlabsAccountCreator()
        thread = threading.Thread(target=creator.run)
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

# Usage
while True:
 if __name__ == "__main__":
    create_accounts(threads)