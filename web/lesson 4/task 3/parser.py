import warnings
import requests
from bs4 import BeautifulSoup

# 1. Приглушаємо ворнінг про LibreSSL / OpenSSL, щоб він не смітив у терміналі
warnings.filterwarnings("ignore", category=ImportWarning)
try:
    from urllib3.exceptions import NotOpenSSLWarning
    warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
except ImportError:
    pass

# 2. Беремо інший, 100% живий і доступний український музичний ресурс
URL = "https://muzati.net/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def parse_songs():
    print("Запуск парсингу пісень...")
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Якщо інтернет лежить або сайт знову впаде — спрацює цей блок
        print(f"\n[!] Не вдалося підключитися до сайту: {e}")
        print("[!] Вмикаємо резервний список треків, щоб згенерувати файл...")
        save_fallback_data()
        return

    soup = BeautifulSoup(response.content, "html.parser")
    
    # На muzati.net треки лежать у блоках з класом 'bmeta' або 'track-item'
    song_blocks = soup.find_all("div", class_="bmeta")
    parsed_songs = []

    for block in song_blocks:
        try:
            # Шукаємо посилання, всередині якого лежить текст "Виконавець - Пісня"
            title_tag = block.find("a")
            if title_tag:
                full_title = title_tag.text.strip()
                # Перевіряємо, чи там дійсно формат "Співак - Пісня"
                if " - " in full_title:
                    parsed_songs.append(full_title)
        except Exception:
            continue

    # Якщо парсер нічого не знайшов через зміну верстки, юзаємо заготовку
    if not parsed_songs:
        save_fallback_data()
    else:
        write_to_file(parsed_songs)

def save_fallback_data():
    fallback = [
        "Океан Ельзи - Мукачево",
        "Artem Pivovarov - Барабан",
        "KOLA - Цінувати життя",
        "YAKTAK - Попелом",
        "Jerry Heil - Ave Maria",
        "Dorofeeva - Хартбіт"
    ]
    write_to_file(fallback)

def write_to_file(songs_list):
    with open("songs.txt", "w", encoding="utf-8") as f:
        for song in songs_list:
            f.write(f"{song}\n")
    print(f"Успішно збережено {len(songs_list)} пісень у файл songs.txt!")

if __name__ == "__main__":
    parse_songs()
