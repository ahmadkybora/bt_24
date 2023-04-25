import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/bt_24')
sys.path.insert(0,"/var/www/bt_24/venv/lib/python3.9/site-packages")
from Cover import main
application = main()