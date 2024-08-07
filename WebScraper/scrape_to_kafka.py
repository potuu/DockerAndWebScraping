import json
import time
from confluent_kafka import Producer

# Kafka yapılandırması
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker adresi
}

# Kafka Producer oluştur
producer = Producer(conf)

# JSON dosyasından verileri oku
with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Her ürünü Kafka topic'e gönder
for product in products:
    product_json = json.dumps(product)  # JSON formatına çevir
    # Kafka topic'e gönder
    producer.produce('my_topic', value=product_json.encode('utf-8'))
    print(f"Ürün gönderildi: {product['name']}")
    # 1 saniye bekle
    time.sleep(1)

# Kafka'ya gönderimi tamamla
producer.flush()

print("Tüm ürünler Kafka topic'e gönderildi.")

