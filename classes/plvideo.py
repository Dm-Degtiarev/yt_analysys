from classes.video import Video
from googleapiclient.discovery import build
import json


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        """Инициализация: ввод id видео, id плейлиста"""
        super().__init__(video_id)
        youtube = build('youtube', 'v3', developerKey=super().api_key)
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet,contentDetails').execute()

        # Инициализвция атрибутов из JSON
        self.playlist_id = playlist_id
        self.playlist_name = self.playlist['items'][0]['snippet']['title']

    def __str__(self):
        """
        При принте экземпляра возвращает значение в форамате:
        'video_name (playlist_name)'
        """
        return f"{self.video_name} ({self.playlist_name})"
