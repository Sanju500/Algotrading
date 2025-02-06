import logging
from data_manager import RedisManager
from config import MAX_QTY

class OrderManager:
    """Handles order placement and liquidation."""
    
    def __init__(self, xt_api, clientID):
        self.xt_api = xt_api
        self.clientID = clientID
        self.redis = RedisManager()

    def place_order(self, instrument, qty, side, order_type="LIMIT"):
        """Places an order with the given parameters."""
        logging.info(f"Placing {side} order: {instrument}, Qty: {qty}")
        order_data = {
            "instrument": instrument,
            "qty": qty,
            "side": side,
            "order_type": order_type,
        }
        return self.xt_api.place_order(**order_data)

    def liquidate_all(self):
        """Liquidates all open positions."""
        logging.info("Initiating liquidation of all positions...")
        positions = self.xt_api.get_position_netwise()
        for position in positions["result"]["positionList"]:
            instrument = position["ExchangeInstrumentId"]
            qty = abs(int(position["Quantity"]))
            side = "SELL" if qty > 0 else "BUY"
            if qty > 0:
                self.place_order(instrument, qty, side)
