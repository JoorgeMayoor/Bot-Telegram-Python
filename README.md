
# 🤖 Bot-Telegram-Python

Bot de Telegram que notifica automáticamente a un grupo o canal de Telegram cada vez que subes un nuevo video o contenido a tu canal de YouTube.

## 🚀 Características

- Monitorea tu canal de YouTube en busca de nuevos videos o publicaciones.
- Envía notificaciones automáticas a un grupo o canal de Telegram.
- Configuración sencilla y personalizable.
- Código abierto y fácil de adaptar a tus necesidades.

## 📋 Requisitos

- Python 3.7 o superior
- Una cuenta de Telegram y un bot creado con [@BotFather](https://t.me/BotFather)
- Un canal o grupo de Telegram donde quieras recibir las notificaciones
- API Key de YouTube Data v3 ([Guía oficial](https://developers.google.com/youtube/v3/getting-started))

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/JoorgeMayoor/Bot-Telegram-Python.git
   cd Bot-Telegram-Python
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

1. Crea un archivo `.env` o configura las variables necesarias en el script:
   - `TELEGRAM_BOT_TOKEN`: Token de tu bot de Telegram
   - `TELEGRAM_CHAT_ID`: ID del grupo o canal de Telegram
   - `YOUTUBE_API_KEY`: API Key de YouTube
   - `YOUTUBE_CHANNEL_ID`: ID de tu canal de YouTube

2. (Opcional) Ajusta la frecuencia de comprobación y otros parámetros en el script según tus necesidades.

## ▶️ Uso

Ejecuta el bot con:
```bash
python bot-telegram.py
```

El bot comenzará a monitorear tu canal de YouTube y enviará notificaciones automáticas a tu grupo o canal de Telegram cada vez que detecte nuevo contenido.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 🙌 Agradecimientos

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [YouTube Data API](https://developers.google.com/youtube/v3)

---
¡Contribuciones y sugerencias son bienvenidas!
