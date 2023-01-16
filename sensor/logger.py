import logging
import os
from datetime import datetime

#create the log file 
LOG_FILE_NAME = f"{datetime.now().strftime('%M%d%y____%H%M%S')}.log"

#create the log directory 
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#create folder if not available 
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path 

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConf(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    level = logging.INFO
)