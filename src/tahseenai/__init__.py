from . import builder
import logging
name='tahseenai'


logger = logging.getLogger("tahseenAI")
logger.setLevel(logging.INFO)
logger.propagate = False
if not logger.handlers:
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    logger.addHandler(consoleHandler)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    consoleHandler.setFormatter(formatter)


__all__=[
    "builder"
]