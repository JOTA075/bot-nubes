import os
import ProxyCloud

BOT_TOKEN = '5875312101:AAGWYcfXGZDKo_4QJ0dH0EhTWO-D5x0-6-M' #Aqui va el token del bot
API_ID =  17345593 #Tu api id de telegram
API_HASH = '80ae053901c049b519ea5bf0f50e1675' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('STANISLASKI','DRP96','Orisha91').split(';')

static_proxy = 'none' #agrega si kieres tener un proxy statico Con @raydel0307 si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space[] = 0
