from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from utils import wait_for_load

url = "https://www.google.com.br/"
firefox = webdriver.Firefox()
response = firefox.get(url)

print("Esperando a pagina ser totalmente carregada...")
wait_for_load(firefox)
print("Página carregada com sucesso!")

#
sleep(3)
print("Pesquisa o elemento input dentro da página carregada.")
search_input = firefox.find_element(By.NAME, "q")

#
sleep(3)
print("Escreve no campo de texto")
search_input.send_keys("Uélio Nobre")

# Pressiona Enter para realizar a busca
sleep(3)
print("Pressionando enter")
search_input.send_keys(Keys.ENTER)

sleep(10)
firefox.quit()
print("Fim da execução do script.")
