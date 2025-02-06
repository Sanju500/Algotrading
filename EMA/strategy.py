from order_manager import OrderManager
import logging

class TradingStrategy:
    """Base class for trading strategies."""
    
    def __init__(self, order_manager: OrderManager):
        self.order_manager = order_manager

    def execute(self):
        """Executes the strategy. Must be implemented in subclasses."""
        raise NotImplementedError

class BuyStrategy(TradingStrategy):
    """Strategy for buying options."""
    
    def execute(self):
        logging.info("Executing Buy Strategy")
        self.order_manager.place_order("NIFTY", 100, "BUY")

class SellStrategy(TradingStrategy):
    """Strategy for selling options."""
    
    def execute(self):
        logging.info("Executing Sell Strategy")
        self.order_manager.place_order("NIFTY", 100, "SELL")

class StrategyFactory:
    """Factory for creating strategy objects."""
    
    @staticmethod
    def get_strategy(strategy_type, order_manager):
        strategies = {
            "BUY": BuyStrategy,
            "SELL": SellStrategy,
        }
        return strategies[strategy_type](order_manager) if strategy_type in strategies else None
