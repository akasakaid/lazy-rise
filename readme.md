# Lazy-RISE

## Features

✅ Auto-claim faucet

## Support

If you like this project, you can support me by buying me a coffee:

[Support via Sociabuzz](https://sociabuzz.com/fawwazthoerif/tribe)

## Discussion

Join our Telegram group for discussions:

[Telegram Group](https://t.me/sdsproject)

## Captcha Providers

Supported captcha providers:

| Provider | Link  |
|----------|---------------|
| Anti-Captcha | [Link](https://getcaptchasolution.com/iiaiemxamz) |
| 2Captcha | [Link](https://2captcha.com/?from=4688295) |
| Capsolver | [Link](https://dashboard.capsolver.com/passport/register?inviteCode=ejmvauaFFnqt) |

## Proxy Providers

Compatible proxy providers:

1. [Proxy-Cheap](https://app.proxy-cheap.com/r/mlShoy)
2. [DataImpulse](https://dataimpulse.com/?aff=48082)
3. [ProxiesFO](https://app.proxies.fo/ref/c02fda06-da42-f640-7ef7-885127487ef0)

This program only supports HTTP protocol. For proxy format, follow these examples:

For authenticated proxies:
```
# format
http://user:password@proxy_server:proxy_port

# example
http://admin:admin@192.168.1.1:8000
```

For non-authenticated proxies:
```
# format
http://proxy_server:proxy_port

# example
http://192.168.1.1:8000
```

## How to Use the Auto Faucet for Testnet Tokens

### Prerequisites
- Latest Python 3 installed
- Git installed

### Installation
```bash
# Clone repository
git clone https://github.com/akasakaid/lazy-rise.git

# Navigate to project directory
cd lazy-rise

# Install dependencies
pip install -r requirements.txt
```

### Configuration
1. Edit `config.py` file:
   - Fill in captcha provider details (see [Captcha Providers](#captcha-providers))
   - Configure proxy if needed (see [Proxy Providers](#proxy-providers))

2. Select operation mode:
   - **1.) Generate New Wallet** (creates new wallet and saves private key to `privatekeys.txt`)
   - **2.) Use Existing Wallet** (uses wallets stored in `addresses.txt`)

### Running the Program
```bash
python faucet.py
```

> **Important Note**:  
> Each IP address is limited to 1 claim per day. Use proxies to claim multiple times with different wallet addresses.

# Thank You :3