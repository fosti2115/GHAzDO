import requests

base_url = "https://your-jfrog-instance.jfrog.io"
access_token = "cmVmdGtuOjAxOjE3NjQyMzQ5NTQ6ZzVkWjRwNGJiZE9HRXFTOWFueWdFTjdVY05r"

headers = {
    "Authorization": f"Bearer {access_token}",
}

# Pobranie listy repozytoriów
response = requests.get(f"{base_url}/artifactory/api/repositories", headers=headers)
print(response.json())
