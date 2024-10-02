import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', '')
CURRENCY_TOKEN = os.getenv('CURRENCY_TOKEN', '')
URL = f'https://apilayer.net/api/live?access_key={CURRENCY_TOKEN}'
