import dotenv
import os

import requests
import json

dotenv.load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

PLAYLIST_IDS = [
    'PLz7GQsHwn5sohr6fp7GiGgx8uXNNsoKGk', # Ssundee among us playlist
    'PLgYvyT_FA3_wZK4vqRJQqIEbGIcLX56BP', # Socksfor1 among us playlist
    'PLJj5zzmVgNBsLjULq-i37u180q9_is2Sr', # 5up among us playlist
    'PLPOGNgq7o8ZflzCWFRGAtZk7HzBn-85tm', # ItzNathz among us playlist
    'PL3cjHI9IU-ZqYx__FMtTulEorBwR0EZPF', # Biffle among us playlist
    'PL9vdIN8uIrCwCrpJW91zITpP2GDoua9C7', # Corpse among us playlist
    'PLMBYlcH3smRxnYCVSriI7EPMIHtQ-Nlcr', # Jacksepticeye among us playlist
    'PLE5TXcUHTQHIi2PiHp5gAOrF2r5WWhwE-', # Inquisitormaster among us playlist
    'PLyTnhjOTbyOUYMmA8Lb155Cr0PHXZMy51', # Cartoonz among us playlist
    'PLwYRiq-Ob29v2cOGvchzjGeqNGYJJXMUo' # Disguised Toast among us playlist
    ]

BASE_URL = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={}&key={}'

def fetch_video_titles(api_key, playlist_id):
    url = BASE_URL.format(playlist_id, api_key)
    video_titles = []

    while True:
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch data from YouTube.")
            return None
        
        data = response.json()
        for item in data['items']:
            title = item['snippet']['title']
            video_titles.append(title)

        if 'nextPageToken' in data:
            url = BASE_URL.format(playlist_id, api_key) + '&pageToken=' + data['nextPageToken']
        else:
            break

    return video_titles

if __name__ == "__main__":
    for playlist in PLAYLIST_IDS:
        titles = fetch_video_titles(API_KEY, playlist)
        if titles:
            with open('video_titles.txt', 'a', encoding='utf-8') as file:
                for title in titles:
                    file.write(title + '\n')
            print(f"Saved {len(titles)} titles to 'video_titles.txt'")