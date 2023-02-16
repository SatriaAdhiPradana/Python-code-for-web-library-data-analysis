import requests
from bs4 import BeautifulSoup

# URL dari situs web yang ingin dianalisis
url = 'https://www.contohwebsite.com'

# Mengambil sumber halaman web
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Menemukan semua tautan di halaman
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

# Menemukan semua gambar di halaman
images = []
for img in soup.find_all('img'):
    images.append(img.get('src'))

# Menemukan semua teks di halaman
text = soup.get_text()

# Menampilkan hasil analisis
print('Tautan:', links)
print('Gambar:', images)
print('Teks:', text)
