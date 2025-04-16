from .http import http
from .log import log


async def ipinfo(ses):
    url = "https://directory.cookieyes.com/api/v1/ip"
    res = await http(ses=ses, url=url)
    if res is None:
        return None
    ip = res.json().get("ip")
    log(f"ip : {ip}")
    return ip
