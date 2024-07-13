# Kafka Docker Setup

Bu proje, Docker kullanarak Kafka ve Zookeeper kurulumunu ve kullanımını içerir. Aşağıdaki adımları takip ederek Kafka ile etkileşimde bulunabilirsiniz.

## Gereksinimler

- Docker ve Docker Compose yüklü olmalıdır.

## Kurulum Adımları

1. **Proje dizinine git:**

#Docker Compose ile Zookeeper ve Kafka başlat:

docker-compose up -d

# Aktif konteynerleri kontrol et:

docker ps
Bu komutla Kafka konteynerinin container_id’sini öğrenebilirsiniz.
Hata ile karşılaşmamak adına aşağıdaki komutu Container adını girdikten sonra kapatabilirsiniz.

docker stop //container adı//

# Kafka konteynerine bağlan:

docker exec -it kafka /bin/bash

# Yeni bir Kafka topic oluştur:

kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Mesaj göndermeye başla:

kafka-console-producer.sh --topic my-topic --bootstrap-server localhost:9092
Mesaj göndermeyi durdurmak için Ctrl+C tuşlarına basabilirsiniz.

# Gönderilen mesajları dinle:

kafka-console-consumer.sh --topic my-topic --bootstrap-server localhost:9092 --from-beginning

# Topic'i sil:

kafka-topics.sh --delete --topic my-topic --bootstrap-server localhost:9092
