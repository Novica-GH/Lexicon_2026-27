import os
import requests
from dotenv import load_dotenv

# Load GITHUB_TOKEN from .env file
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

url = "https://api.github.com/users/octocat/repos"

# --- 1. REQUEST WITHOUT TOKEN ---
print("--- Request WITHOUT Token ---")
response_no_auth = requests.get(url)
limit_no_auth = response_no_auth.headers.get("X-RateLimit-Limit")
print(f"Status Code: {response_no_auth.status_code}")
print(f"X-RateLimit-Limit: {limit_no_auth}")

print("\n" + "-" * 40 + "\n")

# --- 2. REQUEST WITH TOKEN ---
print("--- Request WITH Token ---")
if not token:
    print("Error: GITHUB_TOKEN not found in .env file.")
else:
    headers = {"Authorization": f"Bearer {token}"}
    response_auth = requests.get(url, headers=headers)
    limit_auth = response_auth.headers.get("X-RateLimit-Limit")
    print(f"Status Code: {response_auth.status_code}")
    print(f"X-RateLimit-Limit: {limit_auth}")


# Terminal:

    #     --- Request WITHOUT Token ---
    # Status Code: 200
    # X-RateLimit-Limit: 60

    # ----------------------------------------

    # --- Request WITH Token ---
    # Status Code: 200
    # X-RateLimit-Limit: 5000