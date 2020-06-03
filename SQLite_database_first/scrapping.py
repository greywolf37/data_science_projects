from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://pokemondb.net/pokedex/all'
table_id = 'pokedex'

response = requests.get(link)

soup = BeautifulSoup(response.text, 'html.parser')

pokemon_table = soup.find_all('table', id = table_id)
list_of_tables = pd.read_html(str(pokemon_table))
pokemon_data = list_of_tables[0]

pokemon_data.to_csv('pokemon_data.csv')

