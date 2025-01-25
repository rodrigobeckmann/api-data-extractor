import requests
from urllib.parse import urljoin


class ApiClient:

    def __init__(
        self,
        url: str,
        headers: dict = None,
    ):
        self.url = url
        self.headers = headers

    @staticmethod
    def _handle_response(
        response: requests.Response,
    ):
        if not response.ok:
            raise Exception(f"Error: {response.status_code}: {response.text}")

    def _make_url(
        self,
        path: str,
    ) -> str:
        return urljoin(self.url, path)

    def _request(
        self,
        url: str,
        method: str,
        data: dict = None,
        params: dict = None,
    ) -> requests.Response:
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            data=data,
            params=params,
        )
        self._handle_response(response)
        return response.json()

    def get(
        self,
        path: str,
        params: dict = None,
    ) -> requests.Response:
        response = self._request(
            url=self._make_url(path),
            method='GET',
            params=params,
        )
        return response

    def post(
        self,
        path: str,
        params: dict = None,
        data: dict = None,
        json: dict = None,
    ) -> requests.Response:
        response = self._request(
            url=self._make_url(path),
            method='POST',
            params=params,
            data=data,
            json=json,
        )
        return response
