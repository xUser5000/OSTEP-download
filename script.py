import requests
import threading
from bs4 import BeautifulSoup

def download_pdf(name: str):
    BASE_URL = "https://pages.cs.wisc.edu/~remzi/OSTEP/"
    BOOK_DIR = './'

    url = BASE_URL + name
    print(f"thread {threading.get_ident()}: downloading {url}...")
    res = requests.get(url)
    
    file_path = BOOK_DIR + name
    with open(file_path, 'wb') as f:
        f.write(res.content)
    
    print(f"thread {threading.get_ident()}: download complete for {name}")


if __name__ == '__main__':
    OSTEP_URL = "https://pages.cs.wisc.edu/~remzi/OSTEP/"
    res = requests.get(OSTEP_URL)

    soup = BeautifulSoup(res.text)
    anchors = soup.find_all('a')
    pdf_names = [
        a.get('href')
        for a in anchors if a.get('href') and a.get('href').endswith('.pdf')
    ]

    for name in pdf_names:
        thread = threading.Thread(target=download_pdf, args=(name,))
        thread.start()
