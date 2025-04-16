import os
import httpx
from .log import log


async def http(ses: httpx.AsyncClient, url, data=None):
    attemp = 0
    while True:
        try:
            if attemp == 100:
                return None
            if data is None:
                res = await ses.get(url=url)
            elif data == "":
                res = await ses.post(url=url)
            else:
                res = await ses.post(url=url, data=data)
            if (
                not os.path.exists("http.log")
                or os.path.getsize("http.log") / 1024 > 1024
            ):
                open("http.log", "w").write("")
            open("http.log", "a", encoding="utf-8").write(
                f"{res.status_code} - {res.text}\n"
            )
            return res
        except httpx.NetworkError as e:
            log(f"http request error : network error {e.request.url} !")
            attemp += 1
            continue
        except httpx.ProxyError:
            log("http request error : proxy error !")
            attemp += 1
            continue
        except httpx.TimeoutException as e:
            log(f"http request error : request timeout {e.request.url} !")
            attemp += 1
            continue
        except httpx.RemoteProtocolError:
            log("http request error : server disconnected without response !")
            attemp += 1
            continue
        except Exception as e:
            log(e)
            attemp += 1
            continue
