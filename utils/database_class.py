import pandas as pd

from data_class import Game

class Database(Game):
    def __init__(self, data, name):
        super().__init__(data, name)
    
    def data_game(self):
        return self.data.query(f'GAME == "{self._name}"')

