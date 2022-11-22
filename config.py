import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5710756534:AAE1ihDreMkihVYNTZ4_XdhXz5cpFXItPps')
API_ID =  os.environ.get('api_id','15158057')
API_HASH = os.environ.get('api_hash','6a7956a4a75bd2ed46a021649e4c9edf')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('LevAndrade93','admin3').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','http://KFGGJJYGJKLHFKYEDIGDYJJEKEFKREEGLFDKLH'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
