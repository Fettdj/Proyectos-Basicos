import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs", {
            "download.default_directory": "\dchrome",
        })
        self.driver = webdriver.Chrome(executable_path=r".\chromedriver.exe", chrome_options=chromeOptions)

    def test_usando_toggle(self):
        driver = self.driver
        driver.get("https://www.frecuento.com/categorias/electrodomesticos/14620/productos/?category=14620&brand=&price__gt=&price__lt=&variants=&attributes=&order_by=&page=1&stock=true&name=electrodomesticos")
        time.sleep(3)

        # Encuentra todos los elementos en el contenedor HTML específico
        container_selector = "#__next > div > div.site-content > div.ps-page--shop.categories-products > div:nth-child(2) > div.ps-layout--shop > div.ps-layout__right > div > div.ps-shopping__content > div.ps-shopping-product > div"
        containers = driver.find_elements(By.CSS_SELECTOR, container_selector)

        # Itera sobre cada elemento en el contenedor y descarga las imágenes y el contenido de texto
        for idx, container in enumerate(containers):
            # Encuentra el elemento de imagen
            img_element = container.find_element(By.CSS_SELECTOR, "div.ts-product.justify-content-md-center > div.ps-product-media")
            img_url = img_element.find_element(By.CSS_SELECTOR, "div.img.col-12.col-md-12 > a > img").get_attribute("src")

            if img_url:
                driver.get(img_url)

                # Espera a que la imagen esté presente en la página
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "img"))
                )

                # Encuentra el elemento de la imagen y guarda la captura de pantalla en un archivo
                image_element = driver.find_element(By.TAG_NAME, "img")
                image_path = os.path.join("./imagenes", f"imagen_{idx}.png")
                with open(image_path, "wb") as img_file:
                    img_file.write(image_element.screenshot_as_png)

                # Regresa a la página principal para continuar con la siguiente imagen
                driver.back()

            # Encuentra el elemento de texto
            text_element = container.find_element(By.CSS_SELECTOR, "div.ts-product.justify-content-md-center > div.ps-product-info")
            text_content = text_element.text.strip()
            print(f"Contenido de texto del elemento {idx}:\n{text_content}\n")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    # Crear la carpeta "imagenes" si no existe
    os.makedirs("./imagenes", exist_ok=True)
    unittest.main()
