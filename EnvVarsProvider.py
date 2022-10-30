from Constants import *
from typing import Dict
from dotenv import load_dotenv
from os import environ

# Provides the varaible data from .env
class EnvVarsProvider:

    def __init__(self):
        load_dotenv()

        self.CRICKET_FRIENDS = {
            environ[YUNHAO] : 60,
            environ[SHUAI]  : 35,
            environ[AUTUMN] : 25,
        }

        self.YT_PREMIUM_FRIENDS = {
            environ[YUNHAO] : 23,
            environ[YUCAO]  : 23,
            environ[YILONG] : 23,
            environ[NING]   : 23,
        }
    
    def get_venmo_acess_token(self):
        return environ[VENMO_ACCESS_TOKEN]

    def get_cricket_username_amount_dict(self) -> Dict:
        return self.CRICKET_FRIENDS
