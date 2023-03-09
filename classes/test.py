class Channel:
    def __init__(self, channel_id, api_key):
        self.channel_id = channel_id
        self.api_key = api_key

class Plalist(Channel):
    def __init__(self, api_key):
        super().__init__(api_key)



x = Plalist(5) # Ошибка, так как мы не включили в инициализацию атрибут channel_id вышестоящего класса
