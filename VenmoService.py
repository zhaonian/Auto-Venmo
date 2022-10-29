from typing import Dict
from venmo_api import Client, PaymentPrivacy

# Wraps Venmo APIs needed by this app.
class VenmoService:
    def __init__(self, access_token):
        self.client = Client(access_token)

    def get_user_id_by_username(self, username):
        user = self.client.user.get_user_by_username(username=username)
        if (user): 
            return user.id
        print("User not found!")
        return None

    def request_money(self, userid, amount, description, callback=None):
        return self.client.payment.request_money(
            amount, description, userid, PaymentPrivacy.PUBLIC, None, callback)

    def request_money_from_group(self, user_payment_map: Dict, description):
        for userid, amount in user_payment_map.items():
            self.request_money(userid, amount, description)
