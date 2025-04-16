import os
import sys
import httpx
import asyncio
import json
from config import apikey, provider,TOKEN
from web3 import Web3, Account
from src.utils import ipinfo, log, http
from src.service import anticaptcha, capsolver, twocaptcha


async def faucet(address, proxy):
    ses = httpx.AsyncClient(proxy=proxy, timeout=1000)
    ip = await ipinfo(ses=ses)
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        # "Content-Type": "application/json",
        "Host": "faucet-api.riselabs.xyz",
        "Origin": "https://faucet.testnet.riselabs.xyz",
        "Referer": "https://faucet.testnet.riselabs.xyz/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    }
    ses.headers.update(headers)
    check_url = f"https://faucet-api.riselabs.xyz/faucet/multi-eligibility?address={address}&tokens={TOKEN}"
    res = await http(ses=ses,url=check_url)
    eligible = res.json().get('results',{}).get(TOKEN,{}).get('eligible')
    if not eligible:
        reason = res.json().get('results',{}).get(TOKEN,{}).get('reason')
        log(reason)
        return False
    ses.headers.update({"Content-Type":"application/json"})
    if provider == "anticaptcha":
        timet, token = await anticaptcha(apikey=apikey)
    elif provider == "twocaptcha":
        timet, token = await twocaptcha(apikey=apikey)
    elif provider == "capsolver":
        timet, token = await capsolver(apikey=apikey)
    else:
        log("you haven't set up a captcha bypass provider!")
        return None
    if token is None:
        return None
    log(f"time to solve : {timet}")
    data = {"address": address, "turnstileToken": token, "tokens": [TOKEN]}
    claim_url = "https://faucet-api.riselabs.xyz/faucet/multi-request"
    res = await http(ses=ses, url=claim_url, data=json.dumps(data))
    if res.status_code != 200:
        message = res.json().get('message')
        if 'CAPTCHA verification failed' in message:
            log('invalid captcha !')
            return None
    success = res.json().get('results')[0].get("success")
    if success:
        log(F"success claim {TOKEN} token !")
        return True
    message = res.json().get("message")
    log(f"failed claim {TOKEN} token, {message}")
    return False


async def main():
    proxies = open("proxies.txt").read().splitlines()
    addresses = open("addresses.txt").read().splitlines()
    banner = ">\n> Auto Claim Faucet RISE Testnet Token\n> Join : @sdsproject\n> "
    menu = "1.) generate new walet\n2.) from addresses.txt\n"
    print(banner)
    print()
    print(f"total proxy : {len(proxies)}")
    print(f"total address : {len(addresses)}")
    print()
    print(menu)
    opt = input("input number : ")
    if opt == "1":
        p = 0
        while True:
            wallet = Account.create()
            privatekey = Web3.to_hex(wallet.key)
            open("privatekeys.txt", "a").write(f"{privatekey}\n")
            address = wallet.address
            open("addresses.txt", "a").write(f"{address}\n")
            log(f"addr : {address}")
            while True:
                proxy = None if len(proxies) <= 0 else proxies[p % len(proxies)]
                result = await faucet(address=address, proxy=proxy)
                if result is None:
                    continue
                p += 1
                break

    elif opt == "2":
        for p, address in enumerate(addresses):
            log(f"addr : {address}")
            proxy = None if len(proxies) <= 0 else proxies[p % len(proxies)]
            while True:
                result = await faucet(address=address, proxy=proxy)
                if result is None:
                    continue
                break
    else:
        print("no number selected, exit !")
        sys.exit()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, EOFError):
        sys.exit()
