import requests

app_token = "ghs_awbQBlMsCHcZPhRiIpe4siSm2ucARG2wklVb"

headers = {
    "Authorization": f"Bearer {app_token}",
    "Accept": "application/vnd.github+json",
}

# Pobranie danych o aplikacji
response = requests.get("https://api.github.com/app", headers=headers)
print(response.json())
