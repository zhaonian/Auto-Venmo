from EnvVarsProvider import EnvVarsProvider
from VenmoService import VenmoService

if __name__ == "__main__":
    # Fetch your access token.
    # access_token = Client.get_access_token(username="", password="")
    # print(access_token)

    provider = EnvVarsProvider()

    venmo_service = VenmoService(provider.get_venmo_acess_token())
    davis = venmo_service.get_user_id_by_username("username")

    # result = venmo_service.request_money(userid=davis, amount=1.23, description="Test")
    # print(result)

    cricket_friends_ids = provider.get_cricket_friends_usernames()
    print(cricket_friends_ids)


    cricket_user_payment_map = {
        davis: 120
    }
    result = venmo_service.request_money_from_group(cricket_user_payment_map, "Venmeow Testing 🐱")
    print(result)
