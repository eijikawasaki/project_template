from .core import ClassTemplate
import sys
import os

import logging
sys.path.insert(0, os.path.abspath('.'))
logging.basicConfig(filename='logs/example.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
