from order_manager import OrderManager
from strategy import StrategyFactory
from websocket_client import MarketDataWebSocket
from config import LOG_FILE
import logging

logging.info("Starting trading system...")

# Simulated API and clientID
xt_api = None  # Replace with actual API instance
clientID = "YourClientID"

# Initialize order manager
order_manager = OrderManager(xt_api, clientID)

# Choose strategy
strategy = StrategyFactory.get_strategy("BUY", order_manager)
if strategy:
    strategy.execute()

# Start WebSocket
websocket = MarketDataWebSocket(token="your_token")
websocket.start()
