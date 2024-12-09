import requests

personal_access_token = "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"

headers = {
    "Authorization": f"token {personal_access_token}",
    "Accept": "application/vnd.github+json",
}

# Pobranie repozytoriów użytkownika
response = requests.get("https://api.github.com/user/repos", headers=headers)
print(response.json())
