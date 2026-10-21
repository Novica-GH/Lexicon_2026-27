# api_client.py
import requests


def get_json(url: str, headers: dict = None, timeout: int = 10):
    
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()