from classes.video import Video


video_1 = Video('9lO06Zxhu88')

def test_init():
    """Тестирует инициализацию"""
    assert video_1.video_name == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video_1.video_id == '9lO06Zxhu88'
    #Динамичные атрибуты. Проверяем что просто объявляются
    assert video_1.view_cnt
    assert video_1.like_cnt


def test_str():
    """Тестирует магический метод __str__"""
    assert video_1.__str__() == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
