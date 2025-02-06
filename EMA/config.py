import logging
import os

# Logging Configuration
LOG_FILE = "trading_log.log"
logging.basicConfig(
    filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Redis Config
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# Order Configuration
MAX_QTY = {
    "NIFTY": 1800,
    "BANKNIFTY": 900,
    "FINNIFTY": 1800,
}

# Other Constants
DATA_PATH = os.path.join(os.getcwd(), "data")
