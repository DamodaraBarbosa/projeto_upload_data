import pandas as pd

class Game:
    def __init__(self, data, name):
        self._data = pd.read_csv(data)
        self._name = name

    @property
    def dataframe(self):
        return self._data

    @property
    def name(self):
        return self._name
