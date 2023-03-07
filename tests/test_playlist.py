from classes.playlist import PlayList


playlist_1 = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')

def test_init():
    """Тестирует инициализацию"""
    assert playlist_1.playlist_id == 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'


def test_total_duration():
    """Тестирует total_duration"""
    assert str(playlist_1.total_duration) == '3:41:01'


def test_show_best_video():
    """Тестирует show_best_video"""
    assert playlist_1.show_best_video() is None
