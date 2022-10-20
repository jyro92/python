from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import datetime
from pytz import timezone
import time


WEB = "http://www.pbclibrary.org/raton/mousercise.htm"
PATH = "C:\chromedriver\chromedriver.exe"
PAGE = {
    "uno"       : [1, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "dos"       : [2, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "tres"      : [3, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "cuatro"    : [4, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "cinco"     : [5, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "seis"      : [6, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "siete"     : [7, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "ocho"      : [8, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "nueve"     : [9, 'Archivo', 'body', 'a', 'input', 'table', 'button'],
    "diez"      : [10, 'Archivo', 'body', 'a', 'input', 'table', 'button']
}

class mouseMove:
    def __init__(self, web, path):
        self.web = web
        self.path = path

    def pages(self,page, namePage):
        driver = webdriver.Chrome(self.path)
        driver.get(self.web)
        driver.maximize_window()
        fecha_y_hora_actuales = datetime.now()
        zona_horaria = timezone('America/Guayaquil')
        fecha_y_hora_gye = fecha_y_hora_actuales.astimezone()
        fecha_y_hora_gye = fecha_y_hora_gye.strftime('%d-%m-%Y')

        # Pagina 1
        container = driver.find_element(By.TAG_NAME, PAGE["uno"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["uno"][4])
        data = []
        data.append(container)
        exportarCSV(namePage+'-1 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-2 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-3 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-4 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-5 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-6 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-7 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-8 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["dos"][3])
        data.append(info)
        exportarCSV(namePage+'-9 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m10")]')
        data.append(info)
        exportarCSV(namePage+'-10 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m11")]')
        data.append(info)
        exportarCSV(namePage+'-11 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m12")]')
        data.append(info)
        exportarCSV(namePage+'-12 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m13")]')
        data.append(info)
        exportarCSV(namePage+'-13 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m14")]')
        data.append(info)
        exportarCSV(namePage+'-14 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m15")]')
        data.append(info)
        exportarCSV(namePage+'-15 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m16")]')
        data.append(info)
        exportarCSV(namePage+'-16 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["uno"][4])
        data.append(info)
        exportarCSV(namePage+'-17 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.TAG_NAME, PAGE["uno"][4])
        data.append(info)
        exportarCSV(namePage+'-18 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, '//button[contains(@type,"submit")]')
        data.append(info)
        exportarCSV(namePage+'-19 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, '//input[contains(@type,"image")]')
        data.append(info)
        exportarCSV(namePage+'-20 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m21")]')
        data.append(info)
        exportarCSV(namePage+'-21 ', data)
        btn.click()

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/a[contains(@href,"m22")]')
        data.append(info)
        exportarCSV(namePage+'-22 ', data)
        btn.click()


        data = []
        time.sleep(1)
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        driver.find_element(By.XPATH, '//img[@onclick="javascript:setCheck(1)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(2)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(3)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(4)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(5)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(6)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(7)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(8)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(9)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(10)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(11)"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//a[@href="javascript:testChecks()"]').click()
        time.sleep(1)

        data.append(info)
        exportarCSV(namePage+'-23 ', data)

        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        driver.find_element(By.XPATH, '//input[@onclick="setCheck(1)"]').click()
        driver.find_element(By.XPATH, '//input[@onclick="setCheck(2)"]').click()
        driver.find_element(By.XPATH, '//input[@onclick="setCheck(3)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(4)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(5)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(6)"]').click()
        driver.find_element(By.XPATH, '//img[@onclick="setCheck(7)"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//a[@href="javascript:testChecks()"]').click()
        time.sleep(1)

        data.append(info)
        exportarCSV(namePage+'-24 ', data)

        time.sleep(1)
        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        # create action chain object
        action = ActionChains(driver)
        btn1 = driver.find_element(By.XPATH, './/img[@name="f1"]')
        btn2 = driver.find_element(By.XPATH, './/img[@name="f2"]')
        btn3 = driver.find_element(By.XPATH, './/img[@name="f3"]')
        btn4 = driver.find_element(By.XPATH, './/img[@name="f4"]')
        btn5 = driver.find_element(By.XPATH, './/img[@name="f5"]')
        btn6 = driver.find_element(By.XPATH, './/img[@name="f6"]')
        btn7 = driver.find_element(By.XPATH, './/img[@name="f7"]')
        btn8 = driver.find_element(By.XPATH, './/img[@name="f8"]')


        # double click the item
        dbck1 = action.double_click(btn1)
        dbck2 = action.double_click(btn2)
        dbck3 = action.double_click(btn3)
        dbck4 = action.double_click(btn4)
        dbck5 = action.double_click(btn5)
        dbck6 = action.double_click(btn6)
        dbck7 = action.double_click(btn7)
        dbck8 = action.double_click(btn8)

        # perform the operation
        dbck1.perform()
        dbck2.perform()
        dbck3.perform()
        dbck4.perform()
        dbck5.perform()
        dbck6.perform()
        dbck7.perform()
        dbck8.perform()

        time.sleep(1)
        driver.find_element(By.XPATH, '//img[@name="advance"]').click()
        time.sleep(1)
        data.append(info)
        exportarCSV(namePage + '-25 ', data)

        time.sleep(1)
        data = []
        info = driver.find_element(By.TAG_NAME, PAGE["dos"][2]).text
        btn = driver.find_element(By.XPATH, './/div[contains(@id,"red-slider")]')

        source1 = driver.find_element(By.XPATH, '//div[contains(@class,"line")]')
        target1 = driver.find_element(By.XPATH, '//div[contains(@class,"handle")]')

        actions2 = ActionChains(driver)
        actions2.drag_and_drop(target1, source1).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, '//a[contains(@href,"m26")]').click()
        data.append(info)
        exportarCSV(namePage + '-26 ', data)


def exportarCSV(namePage, data):
    df_pages = pd.DataFrame({namePage: data})
    df_pages.to_csv(namePage + '.csv', index=False, encoding='latin1')
    print("Se generó exitosamente el archivo ", namePage)


obj = mouseMove(WEB, PATH)
obj.pages(PAGE["dos"][0], PAGE["dos"][1])
