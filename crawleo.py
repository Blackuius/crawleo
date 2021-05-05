print('Iniciando crawleo')

# importar biblioteca para requisições http
import requests

from selenium.webdriver import Firefox
browser = Firefox ()
browser.set_window_position(0, 0)
browser.set_window_size(1300, 850)

#entra na url
browser.get('url do site')
#tira print
browser.save_screenshot('/pastadestino.png')
print('print site')
from time import sleep
sleep(1)

#iniciar encerramento do programa
print('Execucao concluida com sucesso')
for cont in range(1, -1, -1):
    sleep(1)
print('encerrando crawleo')
for cont in range(1, -1, -1):
    sleep(1)

browser.quit()


#inicio do envio da mensagem via telegram
def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)
# token único utilizado para manipular o bot (não deve ser compartilhado)
token = 'token'
# id do chat que será enviado as mensagens
chat_id = 'id'
# mensagem
msg = "msg"
# enviar a mensagem
send_message(token, chat_id, msg)

print('mensagem enviada com sucesso')

#fim
