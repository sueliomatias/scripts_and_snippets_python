from selenium import webdriver

# url da página web a ser capturada
url = 'https://www.python.org'

# criar uma nova instância do driver do Chrome
driver = webdriver.Chrome()

# navegar para a página web
driver.get(url)

# tirar um screenshot
driver.save_screenshot('screenshot.png')

# fechar o navegador
driver.quit()

print("Screenshot salvo com sucesso.")