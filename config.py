import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5380969019:AAFoogPZeGjZIcl2SXjPNS3ck2Tkwfx03GQ')
API_ID =  os.environ.get('api_id','15158057')
API_HASH = os.environ.get('api_hash','6a7956a4a75bd2ed46a021649e4c9edf')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('YosmelGarcia','').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','socks5h://KHDGKDYGJDJFGJYHJHGKGEYIKGGGDERJCDLEFHLE'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
