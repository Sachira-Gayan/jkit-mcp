from fastmcp import FastMCP
import httpx
from config import header
app = FastMCP("http-client-server")

# ------------------------------
# HTTP GET Tool
# ------------------------------
@app.tool()
async def http_get(url: str) -> str:
    """
    Perform an HTTP GET request and return the response text.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.text


# ------------------------------
# HTTP POST Tool
# ------------------------------
@app.tool()
async def http_post(url: str, data: dict) -> str:
    """
    Perform an HTTP POST request with JSON body.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data,headers=header)
        response.raise_for_status()
        return response.text


# ------------------------------
# Call any API (headers + query)
# ------------------------------
@app.tool()
async def http_request(
    url: str,
    method: str = "GET",
    headers: dict = None,
    params: dict = None,
    json_body: dict = None,
) -> str:
    """
    A flexible tool for GET/POST/PATCH/DELETE etc.
    """
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json_body
        )
        response.raise_for_status()
        return response.text


if __name__ == "__main__":
    app.run()
