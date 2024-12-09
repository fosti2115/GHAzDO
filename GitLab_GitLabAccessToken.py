import requests

base_url = "https://gitlab.com"
access_token = "glpat-zEeu7ngy68Jyy9ykm3qc"

headers = {
    "Authorization": f"Bearer {access_token}",
}

# Pobranie listy projektów użytkownika
response = requests.get(f"{base_url}/api/v4/projects", headers=headers)
print(response.json())
