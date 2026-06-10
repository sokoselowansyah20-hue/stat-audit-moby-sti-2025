import requests

def get_pull_requests(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all"

    response = requests.get(url)

    return response.json()
