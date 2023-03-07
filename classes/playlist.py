from classes.plvideo import PLVideo
from classes.channel import Channel, YouTube
from googleapiclient.discovery import build
import isodate
import json
import datetime


class PlayList(PLVideo, YouTube):
    def __init__(self, playlist_id: str):
        """Инициализация"""
        self.youtube = build('youtube', 'v3', developerKey=super().api_key)
        self.playlist = self.youtube.playlists().list(id=playlist_id, part='contentDetails,snippet').execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.playlist_id = playlist_id
        self.playlist_name = self.playlist['items'][0]['snippet']['title']
        self.playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        print(json.dumps(self.playlist_videos, indent=2, ensure_ascii=False))

    @property
    def total_duration(self):
        """Возвращает время всего плейлиста"""
        videos_list = [ video['contentDetails']['videoId'] for video in self.playlist_videos['items'] ]
        total_duration = datetime.timedelta()

        for video in videos_list:
            self.video = self.youtube.videos().list(id=video, part='snippet,statistics,contentDetails').execute()
            for duration in self.video['items']:
                total_duration += isodate.parse_duration(duration['contentDetails']['duration'])

        return total_duration

    def show_best_video(self):
        """Печатает ссылку на самое популярное видео из плейлиста (по лайкам)"""
        videos_list = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        popular_video = ''
        total_likes = 0

        for video in videos_list:
            self.video = self.youtube.videos().list(id=video, part='snippet,statistics,contentDetails').execute()
            for id in self.video['items']:
                if int(id['statistics']['likeCount']) > total_likes:
                    total_likes = int(id['statistics']['likeCount'])
                    popular_video = f"https://youtu.be/{id['id']}"

        print(popular_video)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        print(json.dumps(self.playlist, indent=2, ensure_ascii=False))