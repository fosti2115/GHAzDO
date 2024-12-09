from google.cloud import storage
from google.oauth2 import service_account

# Ustawienie poświadczeń
private_key_id = '30a803f62a5184bc69fe46e20b00a2f7f6bf06b1'

credentials = service_account.Credentials.from_service_account_info(
    {'private_key_id': private_key_id, 'other_fields': 'XXX'}
)

# Tworzenie klienta do Google Cloud Storage
storage_client = storage.Client(credentials=credentials)

# Wylistowanie bucketów w Google Cloud Storage
buckets = storage_client.list_buckets()
for bucket in buckets:
    print(bucket.name)
