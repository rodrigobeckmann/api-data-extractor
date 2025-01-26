from api_extractor.client import ApiClient


class ExampleApiClient(ApiClient):

    BASE_URL = "https://datausa.io/api/"

    def __init__(self):
        super().__init__(self.BASE_URL)

    def get_data(
        self,
        params: dict,
    ) -> dict:
        return self.get("data", params=params)
