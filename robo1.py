from selenium import webdriver
from selenium.webdriver.common.Keys import Keys
import time

print("Inciando nosso robô...\n")
driver = webdriver.Chrome("C:\Users\diego.duarte\Desktop\chromedriver_win32")
driver.get("https://registro.br/")
time.sleep(2)
driver.close()