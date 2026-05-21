import json
import requests

URL = "https://api.jikan.moe/v4/top/anime"

def get_popular_anime():
    try:
        response = requests.get(URL)
        response.raise_for_status() 
        
        data = response.json()
        anime_list = data.get('data', [])
        
        result = []
        for anime in anime_list:
            title = anime.get('title_english') or anime.get('title')
            score = anime.get('score')
            
            result.append({
                "title": title,
                "rating": score
            })
            
        with open('popular_anime.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
            
        print("Дані про популярні аніме успішно збережені в popular_anime.json")
        
    except requests.exceptions.RequestException as e:
        print(f"Сталася помилка при запиті до API: {e}")

if __name__ == "__main__":
    get_popular_anime()