import datetime
import threading
from colorama import Fore, Style, init
import os
print_lock = threading.Lock()
class Console:
    def __init__(self) -> None:
        init(autoreset=True)
        self.colors = {
            "green": Fore.GREEN,
            "red": Fore.RED,
            "yellow": Fore.YELLOW,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE,
            "black": Fore.BLACK,
            "reset": Style.RESET_ALL,
            "lightblack": Fore.LIGHTBLACK_EX,
            "lightred": Fore.LIGHTRED_EX,
            "lightgreen": Fore.LIGHTGREEN_EX,
            "lightyellow": Fore.LIGHTYELLOW_EX,
            "lightblue": Fore.LIGHTBLUE_EX,
            "lightmagenta": Fore.LIGHTMAGENTA_EX,
            "lightcyan": Fore.LIGHTCYAN_EX,
            "lightwhite": Fore.LIGHTWHITE_EX
        }

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S") 
    
    def Mode(self, message, obj=""):
        with print_lock:
         print(f"{self.colors['lightblack']}{self.timestamp()} » {self.colors['lightyellow']}MODE{self.colors['lightblack']} {self.colors['lightred']}{message} {self.colors['lightblack']}{self.colors['white']},{self.colors['lightblack']}Value={self.colors['white']}{self.colors['lightmagenta']}{obj}{self.colors['white']}{self.colors['reset']}")
    def sexy(self, message, obj=""):
        with print_lock:
         print(f"{self.colors['lightblack']}{self.timestamp()} » {self.colors['lightcyan']}GENERATED {self.colors['lightblack']} {self.colors['lightgreen']}{message} {self.colors['lightblack']}{self.colors['white']}:{self.colors['lightblack']}Value={self.colors['white']}{self.colors['lightmagenta']}{obj}{self.colors['white']}{self.colors['reset']}")
    def captcha(self, message, obj=""):
        with print_lock:
         print(f"{self.colors['lightblack']}{self.timestamp()} » {self.colors['lightcyan']}SOlVED{self.colors['lightblack']}➜ {self.colors['white']}{message} {self.colors['lightgreen']}{obj}{self.colors['white']} {self.colors['reset']}")
    def Subscribed(self, message, obj=""):
        with print_lock:
         print(f"[{self.colors['lightblack']}{self.timestamp()}] [{self.colors['lightmagenta']}${self.colors['lightblack']}] - {self.colors['white']}{message} {self.colors['lightmagenta']}{obj}{self.colors['white']} {self.colors['reset']}")
    def success(self, message, obj=""):
        with print_lock:
         print(f"[{self.colors['lightblack']}{self.timestamp()}] [{self.colors['lightgreen']}${self.colors['lightblack']}] - {self.colors['white']}{message} {self.colors['lightmagenta']}{obj}{self.colors['white']} {self.colors['reset']}")
    def register(self, message, obj=""):
       with print_lock:
        print(f"[{self.colors['lightblack']}{self.timestamp()}] [{self.colors['lightmagenta']}${self.colors['lightblack']}] - {self.colors['white']}{message} {self.colors['lightgreen']}{obj}{self.colors['white']} {self.colors['reset']}")

    def error(self, message, obj=""):
        with print_lock:
         print(f"[{self.colors['lightblack']}{self.timestamp()}] [{self.colors['yellow']}!{self.colors['lightblack']}] - {self.colors['white']}{message} {self.colors['yellow']}{obj}{self.colors['white']} {self.colors['reset']}")

    def warning(self, message, obj=""):
        with print_lock:
         print(f"{self.colors['lightblack']}{self.timestamp()} » {self.colors['lightyellow']}WARN    {self.colors['lightblack']}➜ {self.colors['white']}{message} {self.colors['lightyellow']}{obj}{self.colors['white']} {self.colors['reset']}")
    def captcha(self, message, obj=""):
       with print_lock:
        print(f"[{self.colors['lightblack']}{self.timestamp()}] [{self.colors['lightgreen']}${self.colors['lightblack']}] - {self.colors['white']}{message} {self.colors['lightcyan']}{obj}{self.colors['white']} {self.colors['reset']}")

    def info(self, message, obj=""):
        with print_lock:
         print(f"[{self.colors['lightblack']}{self.timestamp()}] [{self.colors['lightcyan']}>{self.colors['lightblack']}] - {self.colors['white']}{message} {self.colors['lightcyan']}{obj}{self.colors['white']} {self.colors['reset']}")

    def custom(self, message, obj, color):
        with print_lock:
         print(f"{self.colors['lightblack']}{self.timestamp()} » {self.colors[color.upper()]}{color.upper()} {self.colors['lightblack']}➜ {self.colors['white']}{message} [{self.colors[color.upper()]}{obj}{self.colors['white']}] {self.colors['reset']}")

    def input(self, message):
        with print_lock:
         return input(f"{self.colors['lightblack']}{self.timestamp()} » {self.colors['lightcyan']}INPUT   {self.colors['lightblack']}➜ {self.colors['white']}{message}{self.colors['reset']}")
    def locked(self, message, obj=""):
        with print_lock:
         print(f"{self.colors['lightblack']}{self.timestamp()} » {self.colors['lightyellow']}LOCKED   {self.colors['lightblack']}➜ {self.colors['white']}{message} [{self.colors['lightblue']}{obj}{self.colors['white']}] {self.colors['reset']}")
