from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Ustawienie poświadczeń (OAuth 2.0)
client ID = '659541405857-qbpi4m3tojtfcrk9dkb7e9e8l2cpm1jg.apps.googleusercontent.com'
client secret = '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'

# Przeprowadzenie procesu autoryzacji
flow = InstalledAppFlow.from_client_secrets_file(
    oauth_credentials,
    scopes=['https://www.googleapis.com/auth/drive.file']
)

# Uzyskanie tokenu dostępu
creds = flow.run_local_server(port=0)

# Utworzenie klienta API, np. Google Drive API
drive_service = build('drive', 'v3', credentials=creds)

# Wylistowanie plików na koncie Google Drive
results = drive_service.files().list(pageSize=10).execute()
items = results.get('files', [])
if not items:
    print('No files found.')
else:
    for item in items:
        print(f'{item["name"]} ({item["id"]})')
