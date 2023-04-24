import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/bt_24')
from Cover import main
application = main()