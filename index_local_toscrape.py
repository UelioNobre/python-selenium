from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from utils import wait_for_load
from time import sleep

url = "https://books.toscrape.com/"


def scrape(url):
    print(f"Scrape url: {url}")

    options = Options()
    options.add_argument("--headless")

    firefox = webdriver.Firefox(options=options)
    firefox.get(url)
    wait_for_load(firefox)
    print("Carregamento completo feito com sucesso!")

    print("Percorrendo resultados")
    for book in firefox.find_elements(By.CLASS_NAME, "product_pod"):

        item = {}
        item["title"] = (
            book.find_element(By.TAG_NAME, "h3")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("innerHTML")
        )

        item["price"] = (
            book.find_element(By.CLASS_NAME, "product_price")
            .find_element(By.CLASS_NAME, "price_color")
            .get_attribute("innerHTML")
        )

        item["link"] = (
            book.find_element(By.CLASS_NAME, "image_container")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("href")
        )

        print("Item raspado: ", item)
        sleep(0.5)

    sleep(5)
    print("Fechando navegados")
    firefox.quit()


print("Começou!")
scrape(url)
