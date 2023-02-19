import json
import os
from googleapiclient.discovery import build


class Channel:
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str, api_key: str=api_key) -> None:
        """
        Инициализация: ввод id канала,
        токена (По умолчанию берется переменнная среды YT_API_KEY)
        """
        self.channel_id = channel_id


    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале
        """
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))


