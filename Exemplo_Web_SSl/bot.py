"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from botcity.web.browsers.firefox import default_options

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():

    bot = WebBot()

    # Configurando modo Headless ou não
    bot.headless = False

    # Selecionando Firefox
    bot.browser = Browser.FIREFOX

    # Descomente para configurar o caminho do webdriver
    bot.driver_path = r"C:\Users\dsg02\OneDrive\Documentos\GitHub\botcity\Exemplo_Web_SSl\resources\geckodriver.exe"

    # Caminho para a pasta com o certificado
    certificate_db_path = r"C:\Users\dsg02\OneDrive\Documentos\GitHub\botcity\Exemplo_Web_SSl\resources"

    # Obtendo opcoes padrão com pasta do banco de dados NSS
    # como pasta de usuario do navegador
    options = default_options(
        headless=bot.headless,
        user_data_dir=certificate_db_path
    )

    # Configurando as opções no navegador
    bot.options = options

    # Website de teste de certificado badssl.com.
    bot.browse("https://client.badssl.com/")

    # Aguardando 5 segundos antes de encerrar
    bot.sleep(5000)

    # Encerrando e liberando recursos
    bot.stop_browser()



def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
