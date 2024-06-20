
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

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    

    bot.execute(r"C:\Program Files (x86)\Programas RFB\Sicalc Auto Atendimento\SicalcAA.exe")


    if not bot.find( "btn_continuar", matching=0.97, waiting_time=10000):
        not_found("btn_continuar")
    bot.click()
    
    if not bot.find( "btn_funcoes", matching=0.97, waiting_time=10000):
        not_found("btn_funcoes")
    bot.click()
    
    if not bot.find( "btn_prencher_darf", matching=0.97, waiting_time=10000):
        not_found("btn_prencher_darf")
    bot.click()
    
    if not bot.find( "receita_cod", matching=0.97, waiting_time=10000):
        not_found("receita_cod")
    bot.click()
    
    bot.paste("5629")

    bot.tab()

    # Espera para os campos carregarem
    bot.wait(1000)
    
    if not bot.find( "periodo_apuracao", matching=0.97, waiting_time=10000):
        not_found("periodo_apuracao")
    bot.click()
    
    bot.paste("310120")
    
    
    if not bot.find( "valor", matching=0.97, waiting_time=10000):
        not_found("valor")
    bot.click()
    
    
    # Inserindo valor
    bot.paste("10000")
    
    if not bot.find( "btn_calcular", matching=0.97, waiting_time=10000):
        not_found("btn_calcular")
    bot.click()
    
    if not bot.find( "btn_darf", matching=0.97, waiting_time=10000):
        not_found("btn_darf")
    bot.click()
    
    if not bot.find( "placeholder_nome", matching=0.97, waiting_time=10000):
        not_found("placeholder_nome")
    bot.click()
    
    
    bot.paste("Petrobras")
    
    if not bot.find( "palceholder_tel", matching=0.97, waiting_time=10000):
        not_found("palceholder_tel")
    bot.click()
    
    bot.paste("1199991234")
    
    if not bot.find( "placeholder_cnpj", matching=0.97, waiting_time=10000):
        not_found("placeholder_cnpj")
    bot.click()
    
    bot.paste("33000167000101")
    
    if not bot.find( "placeholder_ref", matching=0.97, waiting_time=10000):
        not_found("placeholder_ref")
    bot.click()
    
    bot.paste("0")
    
    
    if not bot.find( "btn_imprimie", matching=0.97, waiting_time=10000):
        not_found("btn_imprimie")
    bot.click()
    
    
    if not bot.find( "btn_salvar", matching=0.97, waiting_time=10000):
        not_found("btn_salvar")
    bot.click()
    
    
    bot.paste(r"C:\Users\dsg02\OneDrive\Documentos\GitHub\botcity\Exemplo_1\exemplo_1.pdf")
    
    bot.enter()

    bot.wait(1000)

    
    bot.alt_f4()

    bot.alt_f4()

   
    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

















