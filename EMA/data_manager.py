import redis
import os
import ast
import json
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, DATA_PATH

class RedisManager:
    """Singleton class to manage Redis connections."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedisManager, cls).__new__(cls)
            cls._instance.redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
        return cls._instance

    def get_value(self, key: str):
        """Get a value from Redis."""
        return self.redis.get(key)

    def get_keys(self):
        """Get all keys from Redis."""
        return self.redis.keys()

class FileManager:
    """Handles file operations."""
    @staticmethod
    def read_file(filename: str) -> dict:
        """Reads a file and returns a dictionary."""
        filepath = os.path.join(DATA_PATH, filename)
        if os.path.exists(filepath) and os.stat(filepath).st_size > 0:
            with open(filepath, "r") as f:
                return ast.literal_eval(f.read())
        return {}

    @staticmethod
    def save_to_file(filename: str, data: dict):
        """Saves a dictionary to a file."""
        with open(os.path.join(DATA_PATH, filename), "w") as f:
            json.dump(data, f, indent=4)
