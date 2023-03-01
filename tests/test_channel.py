from classes.channel import Channel


def test_str():
    """Тестирует магически метод __str__"""
    ch_1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert str(ch_1) == 'Youtube-канал: вДудь'


def test_add():
    """Тестирует магически метод __add__"""
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch2 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert ch1 + ch2 == ch1.subscriber_cnt + ch2.subscriber_cnt


def test_lt():
    """тестирует магически метод __lt__"""
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch2 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch2.subscriber_cnt += 1
    assert bool(ch1 < ch2) is True
    assert bool(ch1 > ch2) is False
