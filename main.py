from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def start():
  print('call')
  url = 'https://gvtech.co.jp/'
  driver.get(url)
  time.sleep(1)
  try:
    ul = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'global-nav')))
    lis = ul.find_elements(By.TAG_NAME,'li')
    lis[3].click()
    time.sleep(1)
    phone = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CLASS_NAME,'number')))
    print(phone.text)
    return phone

  except TimeoutException as te:
    print(te)

start()


