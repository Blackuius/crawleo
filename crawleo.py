print('Getting Started bot')
# import libraries
import requests
from selenium.webdriver import Firefox
browser = Firefox ()
######----screen position----##########
browser.set_window_position(0, 0)
######----screen size----##########
browser.set_window_size(1300, 850)
#####-------starting list of sites--------######
##############---site---####################
browser.get("http://www.site.com");
browser.save_screenshot('/home/sitephoto.png')
print('print site')
site={'photo':open('//home/sitephoto.png','rb')}
resp = requests.post('https://api.telegram.org/bot<<token>>/sendPhoto?chat_id=<<chat_id>>',files=site)
print('print Sent')
#########----start program shutdown----#########
print('Execution completed successfully')
print('Shutting down bot')
browser.quit()
#start sending the message via telegram
def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Error in sendMessage:", e)
# unique token used to manipulate the bot (must not be shared)
token = '<<token>>'
# chat id to send messages
chat_id = '<<chat_id>>'
# message
msg = "<<msg>>"
# send the message
send_message(token, chat_id, msg)
# message
print('Message sent successfully')
#end
