import json
from classes.channel import Channel, YouTube
from googleapiclient.discovery import build


class Video(Channel, YouTube):
    def __init__(self, video_id) -> None:
        """Инициализация: ввод id видео"""
        youtube = build('youtube', 'v3', developerKey=super().api_key)
        self.video = youtube.videos().list(id=video_id, part='snippet,statistics,contentDetails').execute()

        # Инициализвция атрибутов из JSON
        self.video_id = video_id
        self.video_name = self.video['items'][0]['snippet']['title']
        self.like_cnt = int(self.video['items'][0]['statistics']['likeCount'])
        self.view_cnt = int(self.video['items'][0]['statistics']['viewCount'])

    def __str__(self):
        """При принте экземпляра возвращает значение в форамате 'video_name' """
        return f"{self.video_name}"

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        print(json.dumps(self.video, indent=2, ensure_ascii=False))
