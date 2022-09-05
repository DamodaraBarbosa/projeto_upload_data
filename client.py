from data_class import Game
from utils.database_class import Database
import pandas as pd
import numpy as np

data_gamepass = 'utils\data_gamepass_tratado.csv'
# print(data_gamepass)

game = str(input('What game do you want to search? '))
gamepass = Database(data_gamepass, game)

print(gamepass.top_ranking())

