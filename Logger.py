import os,sys
import datetime
import logging



log_file_name=f"{datetime.datetime.now().strftime('%H:%M:%S _ %d_%m_%Y')}.log"

log_path=os.path.join(os.getcwd(),"Logs",log_file_name)
os.makedirs(log_path,exist_ok=True)

log_file_path=os.path.join(log_path,log_file_name)

log_format="[%(asctime)s] %(levelname)s - %(name)s -%(filename)s -%(lineno)d -%(message)s"

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format=log_format
)