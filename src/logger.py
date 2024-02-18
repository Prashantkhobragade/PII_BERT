import logging
import os
from datetime import datetime

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

LOG_FILE: str = f"{TIMESTAMP}.log"

logs_path = os.path.join(os.getcwd(), "logs", TIMESTAMP)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
