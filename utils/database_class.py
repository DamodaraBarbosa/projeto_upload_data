import pandas as pd
from datetime import datetime as dt
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
        
        # data_of_game.index retorna 'pandas.core.indexes.numeric.Int64Index', o uso do [0] seleciona apenas 
        # o valor do index, também se instancia a variável game_index
        game_index = data_of_game.index[0]
        
        # o uso de game_index garante que seja selecionado o jogo procurado e assim se determine o tempo no Gamepass
        return f'{self._name} has been {abs(dt.today() - data_of_game["ADDED"][game_index]).days} days on Xbox Gamepass.'
    
    def top_ranking(self):
        top_10 = self._data.sort_values('GAMERS', ascending= False)[0:10]

        # para que o index fique do 1º ao 10º, faz-se uma pequena modificação
        top_10.index.name = range(1, 11)

        return top_10
    
