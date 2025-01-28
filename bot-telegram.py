import requests
from googleapiclient.discovery import build

# Configura tus credenciales
YOUTUBE_API_KEY = 'TU_YOUTUBE_API_KEY'
TELEGRAM_BOT_TOKEN = 'TU_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHANNEL_ID = '@tu_canal_de_telegram'

# Función para obtener el último video de un canal de YouTube
def get_latest_video(channel_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    # Obtener la lista de videos del canal
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        order='date',
        maxResults=1
    )
    response = request.execute()
    
    # Extraer información del video
    if response['items']:
        video = response['items'][0]
        video_title = video['snippet']['title']
        video_link = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
        return video_title, video_link
    return None, None

# Función para enviar un mensaje a Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response.json()

# ID del canal de YouTube (puedes obtenerlo desde la URL del canal)
CHANNEL_ID = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'  # Reemplaza con el ID de tu canal

# Obtener el último video y enviar el mensaje
video_title, video_link = get_latest_video(CHANNEL_ID)
if video_title and video_link:
    message = f"Nuevo video: {video_title}\nMira aquí: {video_link}"
    send_telegram_message(message)
    print("Mensaje enviado a Telegram.")
else:
    print("No se encontró ningún video.")
