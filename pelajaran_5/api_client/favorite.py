from assertpy import assert_that

from pelajaran_5.api_client.base import APIClient


class FavoriteAPI(APIClient):
    def __init__(self, email, password):
        super(FavoriteAPI, self).__init__()
        self.base_url = "https://airportgap.dev-tester.com/api/favorites"
        self.token = self.login(email, password)

    def login(self, email, password):
        token = self.post("https://airportgap.dev-tester.com/api/tokens", data={
            "email": email,
            "password": password
        })
        assert_that(token.status_code).is_equal_to(200)
        assert_that(token.json()).contains_key("token")
        assert_that(token.json().get("token")).is_not_empty()
        return token.json().get("token")

    def get_all(self):
        return self.get(self.base_url)
