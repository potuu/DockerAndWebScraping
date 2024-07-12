
### Web Scraping Projesi ###

Bu proje, belirli bir web sitesinden ürün bilgilerini çekmek için Flask ve BeautifulSoup kullanarak geliştirilmiştir. Ayrıca, Kafka ve Zookeeper ile veri akışını yönetir.

## Başlangıç

### Sanal Ortamı Aktifleştirme
Projenin gereksinimlerini yüklemek için sanal ortamı aktifleştirin:

python -m venv venv
venv/Scripts/activate

# Gereksinimleri Yükleme
Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

pip install -r requirements.txt

### Docker Kullanımı
Uyarı:
Eğer Kafka ve Zookeeper başka bir işlem tarafından kullanılıyorsa, bunları durdurmak için şu komutları çalıştırın:

docker stop kafka zookeeper
docker rm kafka zookeeper

# Docker Compose ile Başlatma
Docker Compose ile hizmetleri başlatmak için:

docker-compose -f docker-compose_task2.yml up -d

# Ürünleri Çekme
Web sitesinden ürün bilgilerini çekmek için:

python scrape-products.py

# Kafka'ya Gönderme
Ürün bilgilerini Kafka'ya göndermek için:

python scrape_to_kafka.py

## Flask API'yi Çalıştırma
Flask uygulamasını başlatmak için:

python api_service.py


## Sanal Ortamı Kapatma
İşlemler tamamlandığında sanal ortamı kapatmak için:

deactivate


### Docker İmajı Oluşturma

# Docker imajını oluşturmak için:

docker build -t my_flask_app .

# Docker Konteynerini Çalıştırma
Oluşturulan Docker imajından bir konteyner başlatmak için:

docker run -p 5000:5000 my_flask_app
P.S. eğer Docker kontenyeri çalışırken hata ile karşılaşırsanız aşağıdaki komutları çalıştırmak bu problemi çözecektir:
docker stop zookeeper kafka
docker rm zookeper kafka


### Notlar
Projenin düzgün çalışabilmesi için gerekli tüm bağımlılıkların yüklü olduğundan emin olun.
Geliştirme sırasında karşılaşabileceğiniz hatalar için ilgili dokümantasyonları kontrol edin.
