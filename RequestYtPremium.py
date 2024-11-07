from EnvVarsProvider import EnvVarsProvider
from VenmoService import VenmoService

if __name__ == "__main__":
    provider = EnvVarsProvider()
    venmo_service = VenmoService(provider.get_venmo_access_token())

    cricket_userid_amount_dict = {
        venmo_service.get_user_id_by_username(username): amount
        for (username, amount) in provider.get_yt_username_amount_dict().items()
    }
    venmo_service.request_money_from_friends(
        cricket_userid_amount_dict, 
        description="""Recurring payment via \nzluan․io/venmeow 🐱"""
    )
