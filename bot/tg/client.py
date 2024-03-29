from enum import Enum

import requests


from bot.tg import dc
from bot.tg.dc import GetUpdatesResponse, SendMessageResponse


class Command(str, Enum):
    GET_UPDATES = "getUpdates"
    SEND_MESSAGE = "sendMessage"


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str) -> str:
        """ URL для запроса к Telegram боту через токен """
        return f'https://api.telegram.org/bot{self.token}/{method}'

    def get_updates(self, offset: int = 0, timeout: int = 60) -> dc.GetUpdatesResponse:
        """ Получение исходящих сообщений от пользователя """
        response = requests.get(self.get_url(
            f'getUpdates?offset={offset}&timeout={timeout}&'
            f'allowed_updates=["update_id","message"]'
        ))
        print(response.json())
        return dc.GET_UPDATES_SCHEMA.load(response.json())

    def send_message(self, chat_id: int, text: str) -> dc.SendMessageResponse:
        """ Получение сообщений от бота """
        url = self.get_url('sendMessage')
        response = requests.post(url, json={'chat_id': chat_id, 'text': text})
        print(response.json())
        return dc.SEND_MESSAGE_SCHEMA.load(response.json())
