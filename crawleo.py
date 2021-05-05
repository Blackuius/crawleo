print('Iniciando crawleo')

# importar biblioteca para requisições http
import requests

from selenium.webdriver import Firefox
anjely = 'https://anjely.com.br'
browser = Firefox ()
browser.set_window_position(0, 0)
browser.set_window_size(1300, 850)

#entra na url
browser.get(anjely)
#tira print
browser.save_screenshot('/home/leonardo/leo/fotossites/anjelyfoto.png')
print('print anjely')
##################################
#novo site
from time import sleep
sleep(1)
browser.get("http://www.anexi.com.br");
browser.save_screenshot('/home/leonardo/leo/fotossites/anexifoto.png')
print('print anexi')
from time import sleep
sleep(1)
##################################
#novo site
from time import sleep
sleep(1)
browser.get("http://www.auada.adv.br");
browser.save_screenshot('/home/leonardo/leo/fotossites/auadafoto.png')
print('print auada')
from time import sleep
sleep(1)
##################################
#novo site
from time import sleep
sleep(1)
browser.get("http://www.bloqueioimediato.com.br");
browser.save_screenshot('/home/leonardo/leo/fotossites/bloqueioimediatofoto.png')
print('print bloqueioimediato')
from time import sleep
sleep(1)
#toda parte sleep para gerenciar a contagem de tempo
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
token = '1712796177:AAFH8TvzEK1Y40oqdsmsbe8DrZE0whsgjKo'
# id do chat que será enviado as mensagens
chat_id = '-585311966'
# mensagem
msg = "Ola anexi prints finalizados, por favor olhar pasta determinada, obrigado"
# enviar a mensagem
send_message(token, chat_id, msg)

print('mensagem enviada com sucesso')

#fim

#github att
