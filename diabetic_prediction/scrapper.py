import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import ast

# To prevent accessing 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = pd.read_csv('data\\diabetic_train.csv')

column_list = data.columns
# dic_of_new_columns = {}

with open('data\\list_of_names.txt', 'r') as f:
    dic_of_new_columns = ast.literal_eval((f.read()))



PATH = 'C:\\Program Files\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://wwwn.cdc.gov/nchs/nhanes/search/default.aspx')


counter = 0
for name in column_list:


    try:
        if name in dic_of_new_columns:
            continue

        search = driver.find_element_by_id('Keyword')
        search.send_keys(str(name))


        search.send_keys(Keys.RETURN)


        for i in range(len(str(name))):
            search.send_keys(Keys.BACK_SPACE)

        try:
            table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'GridView1')))
        except:
            continue

        table = driver.find_element_by_id('GridView1')
        # (table.text.split('\n')[1]).split()
        rows = table.find_elements_by_tag_name('td')

        try:
            dic_of_new_columns[name] = rows[1].text
        except:
            dic_of_new_columns[name] = name

        with open('data\\list_of_names.txt', 'w') as f:
            f.write(str(dic_of_new_columns))
    except:
        time.sleep(5)

    driver.get('https://wwwn.cdc.gov/nchs/nhanes/search/default.aspx')

    print(f'Changed keys are {len(dic_of_new_columns)} / {len(column_list)} ')

    counter += 1
    if counter > 600:
        break


driver.close()

with open('data\\list_of_names.txt', 'w') as f:
    f.write(str(dic_of_new_columns))

    

    

    