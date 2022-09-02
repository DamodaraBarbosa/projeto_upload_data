import pandas as pd
from datetime import date as dt

from data_class import Game

class Database(Game):
    def __init__(self, data, name):
        super().__init__(data, name)
    
    def data_game(self):
        data_of_game = self.data.query(f'GAME == "{self._name}"')

        if data_of_game.index != None:
            return data_of_game
        else:
            return 'The game searched does not exist in our database!'
    
    def data_to_date(self):
        self.data['ADDED'] = pd.to_datetime(self.data['ADDED'])
        data_of_game = self.data.query(f'GAME == "{self._name}"')
        print(self.data.iloc[data_of_game.index]['ADDED'])
        return (dt.today() - self.data.iloc[data_of_game.index]['ADDED'])
        
