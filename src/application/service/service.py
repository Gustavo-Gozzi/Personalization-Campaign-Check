
import UserDomain

class UserService:
    def request_personalization(url, token, secret):
        new_user = UserDomain(url, token, secret)

        new_user.request_mcp()


