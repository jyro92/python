from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


web = "https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=5498ea6a-1ebd-4259-891c-b3b4f263ff69&pf_rd_r=4725MCZZ2QVB7Q7DVN2T"
path = "C:\chromedriver\chromedriver.exe"


driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

#paginacion
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
numPages = pagination.find_elements(By.TAG_NAME, 'li')
lastPage = int(numPages[-2].text)

# Inicializar el almacenamiento
book_title = []
book_author = []
book_length = []

current_page = 1
while current_page <=lastPage:
    time.sleep(2)
    # Localizar el contenedor (container) que contiene todos los audiolibros listados en la pagina
    container = driver.find_element(By.ID, 'product-list-a11y-skiplink-target')
    # Obtener todos los audiolibros listados (el "/" da los nodos hijos)
    products = container.find_elements(By.XPATH, './span/ul/li')

    # Hacer un "bucle for" a la lista de productos (cada "product" representa un audiolibro)
    for product in products:
        # Usamos la funcion "contains" para buscar elementos que contienen un texto en particular, así evitamos construir XPath largos
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)  # Almacenando data en la lista
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

        current_page = current_page +1
        # Localizar el boton siguiente_pagina (next_page) y hacer click en el boton. Si el elemento no esta en la pagina, pasar a la siguiente iteracion
        try:
            next_page = driver.find_element_by_xpath('.//span[contains(@class , "nextButton")]')
            next_page.click()
        except:
            pass


driver.quit()
# Almacenando data en un dataframe y exportando a un archivo CSV
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_best_selling.csv', index=False)
