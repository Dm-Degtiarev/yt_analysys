from classes.plvideo import PLVideo


plvideo_1 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')

def test_init():
    """Тестирует инициализацию"""
    assert plvideo_1.playlist_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'
    assert plvideo_1.video_id == 'BBotskuyw_M'
    assert plvideo_1.playlist_name == 'Литература'


def test_str():
    """Тестирует магически метод __str__"""
    assert plvideo_1.__str__() == 'Пушкин: наше все? (Литература)'
