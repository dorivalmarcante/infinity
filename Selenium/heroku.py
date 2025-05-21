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
# Abre o Chrome e acessa a pagina heroku
driver.get("https://www.heroku.com/")
# Espera 2 segundos para a página carregar
time.sleep(2)
# Aceita os cookies, entra na tela de login, digita user e pass e tenta logar
driver.find_element(By.ID, "onetrust-accept-btn-handler").send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element(By.ID, "logged-out-login").send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element(By.ID, "email").send_keys("tomsmith@gmail.com")
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
time.sleep(1)
driver.find_element(By.NAME, "commit").send_keys(Keys.RETURN)
# Espera 10 segundos para ver o resultado
time.sleep(10)
# Fecha o navegador
driver.quit