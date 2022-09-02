class Game:
    def __init__(self, data, name):
        self.data = data
        self._name = name 

    @property
    def name(self):
        return self._name
