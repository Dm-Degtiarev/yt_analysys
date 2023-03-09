import json
import os
from googleapiclient.discovery import build
from abc import ABC, abstractmethod


class YouTube(ABC):
    """Абстрактный класс"""
    @abstractmethod
    def print_info(self):
        """Выводит информацию о канле/виде/плейлисте в зависимости от класса"""
        pass


class Channel(YouTube):
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str, api_key: str = api_key) -> None:
        """
        Инициализация: ввод id канала,
        токен (По умолчанию берется переменнная среды YT_API_KEY)
        """
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        #Инициализвция атрибутов из JSON
        self._channel_id = channel_id
        self.channel_name = self.channel['items'][0]['snippet']['title']
        self.channel_info = self.channel['items'][0]['snippet']['description']
        self.channel_url = f'https://www.youtube.com/channel/{self._channel_id}'
        self.subscriber_cnt = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.videos_cnt = self.channel['items'][0]['statistics']['videoCount']
        self.views_cnt = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        """Возвращает значение в форамате 'Youtube-канал: channel_name' """
        return f"Youtube-канал: {self.channel_name}"

    def __add__(self, other):
        """При сложении экземпляров класса возвращает сумму подписчиков каналов"""
        return self.subscriber_cnt + other.subscriber_cnt

    def __lt__(self, other):
        """При сравнении экземпляров класса (> или <) возвращает True или False"""
        return self.subscriber_cnt < other.subscriber_cnt

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self) -> str:
        """Возвращает id канала"""
        return self._channel_id

    @staticmethod
    def get_service():
        """возвращает объект для работы с API ютуба"""
        return build('youtube', 'v3', developerKey=Channel.api_key)

    def to_json(self):
        """Сохраняет атрибуты объекта класса в JSON"""
        with open(f'{self.channel_name}.json', 'w') as r:
            r.write(json.dumps(
                {
                    "channel_header": {
                        "channel_id": self.channel_id,
                        "channel_name": self.channel_name,
                        "channel_info": self.channel_info,
                        "channel_url": self.channel_url,
                    },
                    "subscriber_cnt": self.subscriber_cnt,
                    "videos_cnt": self.videos_cnt,
                    "views_cnt": self.views_cnt,
                },
                indent=4, ensure_ascii=False)
            )
