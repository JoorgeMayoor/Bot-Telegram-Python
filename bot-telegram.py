import requests
import time
from datetime import datetime

# Configuración
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = ''
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'
CHANNEL_ID = 'YOUR_CHANNEL_ID'
CHECK_INTERVAL = 300  # Intervalo de comprobación en segundos (5 minutos)

def get_latest_video(channel_id, api_key):
    """Obtiene el video más reciente de un canal de YouTube."""
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            video = data["items"][0]
            return {
                "video_id": video["id"].get("videoId"),
                "title": video["snippet"].get("title"),
                "published_at": video["snippet"].get("publishedAt")
            }
    return None

def send_telegram_message(bot_token, chat_id, message):
    """Envía un mensaje a un chat de Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.status_code == 200

def main():
    last_video_id = None

    while True:
        try:
            latest_video = get_latest_video(CHANNEL_ID, YOUTUBE_API_KEY)

            if latest_video and latest_video["video_id"] != last_video_id:
                # Nuevo video detectado
                last_video_id = latest_video["video_id"]
                video_url = f"https://www.youtube.com/watch?v={last_video_id}"
                message = f"\uD83D\uDD14 ¡Nuevo video en el canal!\n\n{latest_video['title']}\n{video_url}"
                
                if send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message):
                    print(f"[{datetime.now()}] Notificación enviada: {latest_video['title']}")
                else:
                    print(f"[{datetime.now()}] Error al enviar la notificación")

        except Exception as e:
            print(f"[{datetime.now()}] Error: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()