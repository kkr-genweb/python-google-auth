**Python starter** for Google OAuth **using a local server flow**. This pattern will:
✅ Open a Chrome tab for user consent
✅ Receive the auth code back on localhost
✅ Exchange it for tokens
✅ Call a simple Google API to confirm authentication (e.g., get your user email)
✅ Output “Hello, {email}!”

## **REQUIREMENTS / GOALS**

**Use case:**
- Use Google OAuth 2.0 (via google-auth & google-auth-oauthlib)
- Use local webserver flow (localhost redirect URI)
- Must run in Python 3.x
- Must open Chrome for user consent

## **1. HOW-TO: Setup**

**Install dependencies:**
```
uv sync
```

**Create OAuth credentials:**
1. Go to https://console.cloud.google.com/apis/credentials
2. Create a new **OAuth 2.0 Client ID**
3. Choose **Desktop App** OR **Web application** with http://localhost:8080/ as redirect URI
4. Download the JSON (e.g., client_secret.json)

## **2. Minimal starter script**

```
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
```

## **3. Expected Outcome**
- On python your_script.py:
    - A Chrome tab opens to Google’s consent page.
    - You sign in & allow.
    - Your local server gets the auth code.
    - Script prints: ✅ Hello, you@example.com! Authentication was successful.

## **4. Risks & Notes**
- For production, you’ll want to:
    - Store and refresh tokens securely (token.json).
    - Use more restrictive scopes.
    - Secure your client secrets.

- This pattern is **for local dev scaffolding** — fine for CLI apps, dev, and testing.
