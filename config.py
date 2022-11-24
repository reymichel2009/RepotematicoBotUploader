import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5633733895:AAGIGiP5xBaMU4ORO8lp4E6jmFLML27a7xI')
API_ID =  os.environ.get('api_id','15158057')
API_HASH = os.environ.get('api_hash','6a7956a4a75bd2ed46a021649e4c9edf')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('YosmelGarcia','LevAndrade93','YosmelGarcia','mmartinez_23','YasielCL','GaviLocaRX990','EL_Wizard').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','socks5h://KIDJKFYEJDJJGIYEJDGGGKYKKIGDDIRGCJLECGEG'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
