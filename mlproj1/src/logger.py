import logging 
import os
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log" #this will create a log file with the name as the current date and time
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #this will create a logs folder in the current working directory and inside that folder it will create a log file with the name as the current date and time
os.makedirs(logs_path, exist_ok=True) #if logs folder/file is not there then it will create it


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) #this is the path where log file will be stored
logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',  #this is the format of the log message, it will include the time, line number, name of the logger, level of the log message and the log message itself
    level=logging.INFO, #this is the level of the log message, it will log all the messages that are of level INFO and above (INFO, WARNING, ERROR, CRITICAL
    ) 


