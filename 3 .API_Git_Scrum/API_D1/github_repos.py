import os
from dotenv import load_dotenv
from api_client import get_json

# Load environment variables from .env file
load_dotenv()

# Retrieve GITHUB_TOKEN from the environment
token = os.getenv("GITHUB_TOKEN")

if not token:
    print("Error: GITHUB_TOKEN not found in .env file.")
    exit(1)

username = input("Enter a GitHub username: ").strip()

if not username:
    print("Error: Username cannot be empty.")
    exit(1)

# Define API endpoint and authentication headers
url = f"https://api.github.com/users/{username}/repos?sort=pushed&per_page=5"
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

# Make the API call and display repository names
try:
    repos = get_json(url, headers=headers)

    print(f"\n--- Top 5 latest pushed repositories for '{username}' ---")
    if isinstance(repos, list) and len(repos) > 0:
        for repo in repos:
            print(f"- {repo['name']}")
    else:
        print("No public repositories found for this user.")

except Exception as e:
    print(f"Failed to fetch repositories: {e}")


# Terminal: 
    
    #  1.   Enter a GitHub username: octocat

    # --- Top 5 latest pushed repositories for 'octocat' ---
    # - Spoon-Knife
    # - Hello-World
    # - linguist
    # - octocat.github.io
    # - git-consortium


    #   2.  Enter a GitHub username: Novica-GH

    # --- Top 5 latest pushed repositories for 'Novica-GH' ---
    # - Lexicon_2026-27
    # - Lexicon_1_Begining_ARCHIVED