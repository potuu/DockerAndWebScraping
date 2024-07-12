# Temel imaj olarak Python kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinim dosyasını kopyala
COPY requirements.txt .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["python", "api_service.py"]
