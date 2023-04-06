import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import simpledialog, filedialog

def main(url, output_filename):
    chromedriver_path = './chromedriver.exe'

    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s)

    driver.get(url)

    driver.maximize_window()

    # Realiza scrolling hacia abajo de manera incremental
    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")

    i = 1
    while True:
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 0.5
        time.sleep(scroll_pause_time)

        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if screen_height * i > scroll_height:
            break

    # Desplazarse hacia abajo una última vez y esperar a que se carguen los elementos
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(15)

    elements_text = driver.find_elements(By.XPATH, '//a[@class="ps-product__title h6"]')
    elements_price = driver.find_elements(By.XPATH, '//p[@class="price"]')
    elements_img = driver.find_elements(By.XPATH, '//img[@class="img"]')

    min_length = min(len(elements_text), len(elements_price), len(elements_img))

    data = []
    for i in range(min_length):
        product = elements_text[i].text
        price = elements_price[i].text
        img = elements_img[i].get_attribute('src')
        data.append([product, price, img])

    driver.quit()

    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(data, columns=['Producto', 'Precio', 'Imagen'])

    # Extraer el precio original y almacenarlo en una nueva columna
    precio_original_pattern = r'\$(\d+\.\d+)(?=\$)'
    df['Precio en Descuento'] = df['Precio'].apply(
        lambda x: re.search(precio_original_pattern, x).group() if re.search(precio_original_pattern, x) else '')

    # Eliminar el precio original del campo Precio
    df['Precio'] = df['Precio'].apply(lambda x: re.sub(precio_original_pattern, '', x))

    # Guardar el DataFrame en un archivo de Excel

    df.to_excel(output_filename, index=False)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    url = simpledialog.askstring("Entrada", "Por favor, ingrese la URL para hacer web scraping:")

    if url:
        filetypes = [("Excel files", "*.xlsx"), ("All files", "*.*")]
        output_filename = filedialog.asksaveasfilename(title="Guardar como", defaultextension=".xlsx",
                                                       filetypes=filetypes)

        if output_filename:
            main(url, output_filename)
        else:
            print("No se proporcionó un nombre de archivo válido.")
    else:
        print("No se proporcionó una URL válida.")