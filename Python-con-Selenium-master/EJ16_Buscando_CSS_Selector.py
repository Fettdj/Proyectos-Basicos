from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"\chromedriver.exe")
driver.get("https://www.frecuento.com/categorias/mes-de-la-construccion/16965/productos/")
time.sleep(5)
content = driver.find_element_by_css_selector('a.w3-blue')
content.click()