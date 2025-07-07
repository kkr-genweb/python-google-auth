"""
Minimal Google OAuth2 local flow example.
Opens Chrome tab for consent. Prints your email if authenticated.
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# -----------------------------------------------
# CONFIGURATION
# -----------------------------------------------
SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email']
CLIENT_SECRETS_FILE = 'client_secret.json'

# -----------------------------------------------
# MAIN
# -----------------------------------------------

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)

    creds = flow.run_local_server(port=8080)

    service = build('oauth2', 'v2', credentials=creds)

    user_info = service.userinfo().get().execute()
    email = user_info.get('email')

    print(f"✅ Hello, {email}! Authentication was successful.")

if __name__ == '__main__':
    main()