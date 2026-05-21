import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

def parse_top_books():
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Помилка завантаження сторінки: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    top_books = []

    for book in books:
        rating_tag = book.find('p', class_='star-rating')
        if rating_tag and 'Five' in rating_tag.get('class', []):
            title_tag = book.h3.a
            if title_tag and title_tag.get('title'):
                top_books.append(title_tag['title'])

    with open('top_books.txt', 'w', encoding='utf-8') as f:
        for title in top_books:
            f.write(f"{title}\n")

    print(f"Успішно збережено {len(top_books)} книг із рейтингом 5 зірок у top_books.txt")

if __name__ == "__main__":
    parse_top_books()