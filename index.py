from selenium import webdriver
from time import sleep
from utils import wait_for_load


# Adiciona opção de configuração no navegador
options = webdriver.FirefoxOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--start-maximized")
options.add_argument("--window-size=800,600")

# Endereço da máquina virtual Docker e da pagina web
url_executor = "http://localhost:4444/wd/hub"
url = "https://www.python.org/"

# Executando em modo "Marionette"
firefox = webdriver.Remote(command_executor=url_executor, options=options)
response = firefox.get(url)

# Espera a página carregar completamente
wait_for_load(firefox)

print("Página carregada com sucesso!")
sleep(20)

firefox.quit()
print("Fim da execução do script.")
