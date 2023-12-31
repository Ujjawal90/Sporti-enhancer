import requests, json

class SpotifyOauthClient():

    def __init__(self):

        self.CLIENT_ID = "5338801173a54244ab3a5fd6f6070fda"
        self.CLIENT_SECRET = "d1f0a72005144ee6a86ae3b846c31cc8"
        self.REDIRECT_URI = "https://spoti-enhancer-8z82.onrender.com/redirect/"
        self.SCOPE = "user-top-read user-read-private user-follow-read playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private"
        self.OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
        self.OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
    
    def get_auth_url(self):

        payload = {
            "client_id": self.CLIENT_ID,
            "response_type": "code",
            "redirect_uri": self.REDIRECT_URI,
            "scope": self.SCOPE,
        }

        auth_url = requests.get(self.OAUTH_AUTHORIZE_URL, params=payload).url

        return auth_url

    def get_token_info(self, auth_code):

        body = {
            "grant_type": "authorization_code",
            "code": str(auth_code),
            "redirect_uri": self.REDIRECT_URI,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET    
        }

        post = requests.post(self.OAUTH_TOKEN_URL, data=body)
        response_data = json.loads(post.text)

        return response_data

    def refresh_token(self, refresh_token):

        body = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET    
        }

        post = requests.post(self.OAUTH_TOKEN_URL, data=body)
        response_data = json.loads(post.text)
        
        return response_data
