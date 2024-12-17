import logging
#from logging.handlers import RotatingFileHandler
from logging import handlers
import sys

log = logging.getLogger('')
log.setLevel(logging.DEBUG)
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
log.addHandler(ch)

fh = handlers.RotatingFileHandler("log.log", maxBytes=(1048576*5), backupCount=7)
fh.setFormatter(format)
log.addHandler(fh)

log.info("asd")