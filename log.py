import sys

import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
        
logger=logging.getLogger()

sh = logging.StreamHandler(sys.stdout)
# TODO: make the log file location configurable
fh = RotatingFileHandler("db.log", maxBytes = 1000000, backupCount = 30)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
sh.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(sh)
logger.addHandler(fh)

logger.setLevel(logging.WARN)
L = logging.getLogger("DBServer")
L.setLevel(logging.DEBUG)
sh.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

def snip(s):
    u = unicode(s)
    u=u[:128]
    return u.encode('utf8')
