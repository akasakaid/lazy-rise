from datetime import datetime
from colorama import Fore, Style

hitam = Fore.LIGHTBLACK_EX
reset = Style.RESET_ALL


def log(msg):
    now = datetime.now().isoformat(" ").split(".")[0]
    print(f"{hitam}[{now}] {reset}{msg}{reset}")
