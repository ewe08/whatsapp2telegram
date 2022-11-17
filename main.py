import os


from whatsapp_api_client_python import API
from dotenv import load_dotenv

load_dotenv()
ID_INSTANCE = os.getenv('ID_INSTANCE')
API_TOKEN_INSTANCE = os.getenv('API_TOKEN_INSTANCE')
greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)

