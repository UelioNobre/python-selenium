def check_page_loaded(driver):
    return driver.execute_script("return document.readyState") == "complete"


def wait_for_load(driver):
    while not check_page_loaded(driver):
        print("Pagina não carregada")
