
# Lazy-RISE

## Fitur

✅ Auto-claim faucet

## Support

Jika Anda menyukai proyek ini, Anda bisa mendukung saya dengan mentraktir kopi:

[Support via Sociabuzz](https://sociabuzz.com/fawwazthoerif/tribe)

## Diskusi

Bergabunglah dengan grup Telegram untuk berdiskusi:

[Telegram Group](https://t.me/sdsproject)

## Provider Captcha

Berikut provider captcha yang didukung:

| Provider | Link  |
|----------|---------------|
| Anti-Captcha | [Link](https://getcaptchasolution.com/iiaiemxamz) |
| 2Captcha | [Link](https://2captcha.com/?from=4688295) |
| Capsolver | [Link](https://dashboard.capsolver.com/passport/register?inviteCode=ejmvauaFFnqt) |

## Provider Proxy

Provider proxy yang kompatibel:

1. [Proxy-Cheap](https://app.proxy-cheap.com/r/mlShoy) - `(Recommended)`
2. [DataImpulse](https://dataimpulse.com/?aff=48082)
3. [ProxiesFO](https://app.proxies.fo/ref/c02fda06-da42-f640-7ef7-885127487ef0)

Program ini hanya mendukung tipe protokol http. Untuk format proxy bisa mengikuti contoh berikut

Jika proxy menggunakan autentikasi

```
# format
http://user:password@proxy_server:proxy_port

# contoh
http://admin:admin@192.168.1.1:8000
```

Jika proxy tidak menggunakan autentikasi

```
# format
http://proxy_server:proxy_port

# contoh
http://192.168.1.1:8000
```

## Cara Menggunakan Auto Faucet Testnet Token

### Prasyarat
- Python 3 versi terbaru terinstall
- Git terinstall

### Instalasi
```bash
# Clone repository
git clone https://github.com/akasakaid/lazy-rise.git

# Masuk ke direktori proyek
cd lazy-rise

# Install dependencies
pip install -r requirements.txt
```

### Konfigurasi
1. Edit file `config.py`:
   - Isi data provider captcha (lihat [Provider Captcha](#provider-captcha))
   - Konfigurasi proxy jika diperlukan (lihat [Provider Proxy](#provider-proxy))
   - Isi simbol dari token yang ingin diklaim.

2. Pilih mode operasi:
   - **1.) Generate Wallet Baru** (menggenerate wallet baru dan private key akan disimpan di `privatekeys.txt`)
   - **2.) Menggunakan wallet yang sudah ada** (menggunakan wallet yang tersimpan di `addresses.txt`)

### Menjalankan Program
```bash
python faucet.py
```

> **Catatan Penting**:  
> Setiap alamat IP hanya diperbolehkan claim 1x/hari. Gunakan proxy untuk claim berkali-kali dengan alamat wallet berbeda.

# Terima Kasih :3
