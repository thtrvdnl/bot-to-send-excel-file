import logging
import os

env = os.getenv

API_TOKEN = env("TOKEN")

logging.basicConfig(level=logging.INFO)
