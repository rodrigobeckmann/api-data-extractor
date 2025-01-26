import requests
from urllib.parse import urljoin
from typing import Optional


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
    ) -> None:
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
        data: Optional[dict] = None,
        params: Optional[dict] = None,
    ) -> dict:
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
        params: Optional[dict] = None,
    ) -> dict:
        response = self._request(
            url=self._make_url(path),
            method="GET",
            params=params,
        )
        return response

    def post(
        self,
        path: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> dict:
        response = self._request(
            url=self._make_url(path),
            method="POST",
            params=params,
            data=data,
            json=json,
        )
        return response
