from selenium import webdriver
from time import sleep
from utils import wait_for_load

url = "https://www.python.org/"
firefox = webdriver.Firefox()
response = firefox.get(url)

wait_for_load(firefox)

print("Página carregada com sucesso!")
sleep(5)

firefox.quit()
print("Fim da execução do script.")
