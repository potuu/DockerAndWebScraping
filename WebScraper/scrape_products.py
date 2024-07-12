import requests
from bs4 import BeautifulSoup
import json
import time

# Ana sayfa URL'si
BASE_URL = 'https://scrapeme.live/shop/'

# Ana sayfadan ürün başlıklarını ve bağlantılarını çek
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Ürün başlıklarını ve bağlantılarını bul
product_links = [a['href'] for a in soup.select('.woocommerce-LoopProduct-link')]

# Ürün bilgilerini saklamak için liste
products = []

for link in product_links:
    product_response = requests.get(link)
    product_soup = BeautifulSoup(product_response.content, 'html.parser')
    
    # Ürün bilgilerini çek
    name = product_soup.find('h1', class_='product_title entry-title').get_text().strip()
    
    # Fiyatı çek
    price_element = product_soup.find('p', class_='price')
    if price_element:
        price_amount = price_element.find('span', class_='woocommerce-Price-amount amount')
        if price_amount:
            price = price_amount.get_text(strip=True)
        else:
            price = "Fiyat bulunamadı"
    else:
        price = "Fiyat bulunamadı"
        
    description = product_soup.find('div', class_='woocommerce-product-details__short-description').get_text().strip()
    stock = product_soup.find('p', class_='stock in-stock').get_text().strip()
    
    # Ürün bilgilerini sözlüğe ekle
    product_info = {
        'name': name,
        'price': price,
        'description': description,
        'stock': stock
    }
    products.append(product_info)
    
    # 1 saniye bekle
    time.sleep(1)

# Ürün bilgilerini JSON dosyasına kaydet
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print("Ürün bilgileri products.json dosyasına kaydedildi.")
