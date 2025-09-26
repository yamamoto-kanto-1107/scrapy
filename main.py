from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def sum_values(a, b):
    """a と b が同じか確認。違う場合 False を返す"""
    if a != b:
        return False
    return True

def start():
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = 'https://gvtech.co.jp/'
    driver.get(url)
    time.sleep(1)
    try:
        # まず値の確認
        if sum_values(1, 1) == False:
            return False

        # ul要素を取得
        ul = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'global-nav'))
        )
        print('call---')
        print(ul)
        lis = ul.find_elements(By.TAG_NAME,'li')
        lis[3].click()
        time.sleep(1)

        phone = WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.CLASS_NAME,'number'))
        )
        return phone.text

    except TimeoutException:
        return False
start()