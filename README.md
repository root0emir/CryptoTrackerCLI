# Kripto Para Takip Aracı (Crypto Tracker CLI)

Bu araç, komut satırı üzerinden en popüler 10 kripto paranın fiyatlarını canlı olarak takip etmenizi sağlar. Windows ve Linux işletim sistemlerinde çalışabilir.

## Özellikler

- En popüler 10 kripto paranın canlı takibi
- Piyasa değeri, fiyat, 24 saatlik değişim ve hacim bilgileri
- Renkli ve düzenli komut satırı arayüzü
- Özelleştirilebilir yenileme aralığı

## Gereksinimler

- Python 3.6+
- requests
- tabulate
- colorama
- click

## Kurulum

1. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

### Canlı Takip

Kripto para fiyatlarını canlı olarak takip etmek için:

```bash
python crypto_tracker.py live
```

Yenileme aralığını ayarlamak için (örneğin 30 saniye):

```bash
python crypto_tracker.py live --interval 30
# ya da
python crypto_tracker.py live -i 30
```

### Tek Seferlik Görüntüleme

Kripto para fiyatlarını sadece bir kez görüntülemek için:

```bash
python crypto_tracker.py once
```

## Not

Bu araç, CoinGecko API'sini kullanmaktadır ve herhangi bir API anahtarı gerektirmez. Ancak, API kullanım sınırlamaları nedeniyle çok sık yenileme yapmaktan kaçınılmalıdır.

## Kısayollar

- Programı sonlandırmak için: `Ctrl+C`
