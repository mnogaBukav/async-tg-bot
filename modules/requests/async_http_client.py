from aiohttp import ClientSession, ClientResponse
from typing import List, Optional, Dict


class AsyncHTTPClient:
    def __init__(self, session: Optional[ClientSession] = None, 
                 base_url: Optional[str] = None) -> None:
        """Initializes the AsyncHTTPClient.

        Args:
        - session (Optional[ClientSession]): A client session to use. 
        If not provided, a new session will be created.
        - base_url (Optional[str]): The base URL for requests."""
        self.__session = session or ClientSession(base_url=base_url)
        self.base_url = base_url or ''

    async def __request(
            self, method: str, url: str, **kwargs
        ) -> ClientResponse:
        """Internal method to make HTTP requests.

        Args:
        - method (str): The HTTP method (e.g., 'GET', 'POST').
        - url (str): The URL for the request.
        - **kwargs (Any): Additional arguments to pass to the request.

        Returns:
        - ClientResponse: The response from the server."""
        async with getattr(self.__session, method)(url, **kwargs) as r:
            return r

    async def get(
            self, url: str, params: Optional[Dict[str, str]] = None
        ) -> ClientResponse: 
        """Makes a GET request.

        Args:
        - url (str): The URL for the request.
        - params (Optional[Dict[str, str]]): Query parameters to include
        in the request.

        Returns:
        - ClientResponse: The response from the server."""
        return await self.__request('get', url, params=params)

    async def post(
            self, url: str, json: Optional[List[dict]] = None
        ) -> ClientResponse: 
        """Makes a POST request.

        Args:
        - url (str): The URL for the request.
        - json (Any): JSON data to include in the request body.

        Returns:
        - ClientResponse: The response from the server."""
        return await self.__request('post', url, json=json)
    
    async def close_session(self) -> None:
        """Closes the client session.

        Raises:
        - RuntimeError: If the session is already closed."""
        await self.__session.close()
