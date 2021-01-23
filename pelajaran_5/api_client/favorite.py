from pelajaran_5.api_client.base import APIClient


class FavoriteAPI(APIClient):
    def __init__(self):
        self.base_url = "https://airportgap.dev-tester.com/api/favorites"

    def get_all(self):
        return self.get(self.base_url)