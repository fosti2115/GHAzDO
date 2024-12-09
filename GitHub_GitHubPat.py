import requests

personal_access_token = "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"

headers = {
    "Authorization": f"token {personal_access_token}",
    "Accept": "application/vnd.github+json",
}

# Pobranie danych użytkownika
response = requests.get("https://api.github.com/user", headers=headers)
print(response.json())
