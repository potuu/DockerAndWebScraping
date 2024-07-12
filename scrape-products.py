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
product_titles = soup.find_all('h2', class_='woocommerce-loop-product__title')
product_links = [a['href'] for a in soup.select('.woocommerce-LoopProduct-link')]

# Ürün bilgilerini saklamak için liste
products = []

for link in product_links:
    product_response = requests.get(link)
    product_soup = BeautifulSoup(product_response.content, 'html.parser')
    
    # Ürün bilgilerini çek
    name = product_soup.find('h1', class_='product_title entry-title').get_text().strip()
    price = product_soup.find('span', class_='woocommerce-Price-amount amount').get_text().strip()
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
