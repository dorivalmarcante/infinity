from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configura o Chorme para parecer menos automatizado (evitar a detecção como Bot)
options = webdriver.ChromeOptions()
# Desativa flags de automação
options.add_argument("--disable-blink-features=AutomationControlled")
# Inicia o navegador Chrome com as configurações acima
driver = webdriver.Chrome(options=options)
# Abre o Chrome
driver.get("https://www.google.com")
# Espera 2 segundos para a página carregar
time.sleep(2)
# Localiza a barra de pesquisa do Google (nome="q") e digita "Clima hoje" - Keys.RETURN = tecla Enter
#driver.find_element(By.NAME, "q").send_keys("Clima hoje", Keys.RETURN)
driver.find_element(By.NAME, "q").send_keys("Selenium WebDriver", Keys.RETURN)
driver.find_element(By.CLASS_NAME, "VuuXrf").click()
# Espera 5 segundos para ver o resultado
time.sleep(5)
# Fecha o navegador
# driver.quit

