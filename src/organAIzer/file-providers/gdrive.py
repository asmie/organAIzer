import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def get_files():
    # Set up the scopes and credentials
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Call the Drive API
    service = build('drive', 'v3', credentials=creds)

    # Get a list of file IDs
    results = service.files().list().execute()
    files = results.get('files', [])

    if not files:
        print('No files found.')
    else:
        print('Files:')
        for file in files:
            print(file['name'])

# alternative way
# topFolderId = '###' # Please set the folder of the top folder ID.
#
# items = []
# pageToken = ""
# while pageToken is not None:
#     response = service.files().list(q="'" + topFolderId + "' in parents", pageSize=1000, pageToken=pageToken, fields="nextPageToken, files(id, name)").execute()
#     items.extend(response.get('files', []))
#     pageToken = response.get('nextPageToken')
#
# print(items)