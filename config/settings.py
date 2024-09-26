import os
from dotenv import load_dotenv

load_dotenv()

DENODO_HOST = os.getenv('DB_HOST', 'virtualizador.teste.net')
DENODO_PORT = os.getenv('DB_PORT', '5000')
DENODO_DATABASE = os.getenv('DB_DATABASE', 'ldw')
DENODO_USER = os.getenv('DB_USER')
DENODO_PASSWORD = os.getenv('DB_PASSWORD')




