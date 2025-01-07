import requests

# Access Token
access_token = 'EAAXJ5buEshgBOyRjdkR7AN7hwkFEhdjXhuCSNNtQ188ydjoNbPE7azZB44jo6rMP1PjZC1UZABRYF3q6Vy4YtbtpLzFu49cObW1U9P044pG41cMiYSJRmp2fXaZAP9PqZBdKM2fdLMzCwRaT7VZAlXL3v1Y06lt0AOL2zpfKMpMkcBZB8Sr4MIUsTHXZCRJZAqUiFW4ntFkrc1t4GFLo7vd2rabJZCKf8ZAQ8Q8HD4UZD'

# Przykładowe zapytanie do Facebook Graph API
url = 'https://graph.facebook.com/v15.0/me'
params = {
    'access_token': access_token,
    'fields': 'id,name,email'  # Wybór pól do zwrócenia
}
response = requests.get(url, params=params)

if response.status_code == 200:
    print("Dane użytkownika:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
