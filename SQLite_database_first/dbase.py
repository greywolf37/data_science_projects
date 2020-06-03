import sqlite3
import pandas as pd



def create_db(path):
    '''
    Creates the pokemon database
    '''

    conn = sqlite3.connect(path)

    c = conn.cursor()

    # Creating the pokemon table
    c.execute('''CREATE TABLE pokemon (
        ID integer,
        Name text,
        Type text,
        Total integer,
        HP integer,
        Attack integer,
        Defense integer,
        Sp_Atk integer,
        Sp_Def integer,
        speed integer )
        ''')

    conn.commit()

    conn.close()

def insert_table_pd(connector, data):
    '''
    inserts the pandas dataframe into the database
    '''

    c = connector.cursor()

    for index in range(data.shape[0]):
        values = {
        'ID' : int(data['#'][index]),
        'Name' : data['Name'][index],
        'Type' : data['Type'][index],
        'Total' : int(data['Total'][index]),
        'HP' : int(data['HP'][index]),
        'Attack' : int(data['Attack'][index]),
        'Defense' : int(data['Defense'][index]),
        'Sp_Atk' : int(data['Sp. Atk'][index]),
        'Sp_Def' : int(data['Sp. Def'][index]),
        'Speed' : int(data['Speed'][index]),       
        }
        c.execute("INSERT INTO pokemon VALUES (:ID, :Name, :Type, :Total, :HP, :Attack, :Defense, :Sp_Atk, :Sp_Def, :Speed )", values)

    connector.commit()





# # conn = sqlite3.connect('pokemon.db')
# conn = sqlite3.connect(':memory:')

# c = conn.cursor()

# # Creating the pokemon table
# c.execute('''CREATE TABLE pokemon (
#     ID integer,
#     Name text,
#     Type text,
#     Total integer,
#     HP integer,
#     Attack integer,
#     Defense integer,
#     Sp_Atk integer,
#     Sp_Def integer,
#     speed integer )
#     ''')

# conn.commit()


# # Loading the pokemon data
# data = pd.read_csv('pokemon_data.csv')

# for index in range(data.shape[0]):
#     values = {
#     'ID' : data['#'][index],
#     'Name' : data['Name'][index],
#     'Type' : data['Type'][index],
#     'Total' : data['Total'][index],
#     'HP' : data['HP'][index],
#     'Attack' : data['Attack'][index],
#     'Defense' : data['Defense'][index],
#     'Sp_Atk' : data['Sp. Atk'][index],
#     'Sp_Def' : data['Sp. Def'][index],
#     'Speed' : data['Speed'][index],       
#     }
#     c.execute("INSERT INTO pokemon VALUES (:ID, :Name, :Type, :Total, :HP, :Attack, :Defense, :Sp_Atk, :Sp_Def, :Speed )", values)

# conn.commit()

# conn.close()



def main():

    path = 'pokemon.db'

    create_db(path)

    # Loading the pokemon data
    data = pd.read_csv('pokemon_data.csv')

    conn = sqlite3.connect(path)

    insert_table_pd(conn, data)

    conn.close()









if __name__ == "__main__":
    main()