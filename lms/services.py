import requests

from config.settings import URL_TG, TOKEN_BOT


def send_tg_message(tg_chat_id, message):
    params = {
        "text": message,
        "chat_id": tg_chat_id,
    }
    requests.get(f"{URL_TG}{TOKEN_BOT}/sendMessage", params=params)

