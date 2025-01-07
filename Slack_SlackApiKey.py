import requests

# Slack API Key
slack_api_key = 'xoxe.xoxp-1-Mi0yLTMyNjM4Mzg0MTkyNi01OTMwMTMwNzExMTI3LTgyNTQzNjMyOTY1OTctODI4MDAxNzA4NzMxMi04Y2MwZjk4ZGQwZmQzYmRmNzUzM2U5OGMxNjAwYmNiMDY2Nzc5OTIxM2E0NTEwOGViNDZhNzY3OTM3NDE4ZWEw'

# Przykładowe zapytanie do Slack API (np. lista kanałów)
url = 'https://slack.com/api/conversations.list'
headers = {
    'Authorization': f'Bearer {slack_api_key}'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    channels = response.json().get('channels', [])
    print("Kanały Slack:")
    for channel in channels:
        print(f" - {channel['name']}")
else:
    print(f"Error {response.status_code}: {response.text}")
