import spotipy # type: ignore
from spotipy.oauth2 import SpotifyClientCredentials 


def setup_spotify_authentication(client_id, client_secret):
    """
    Set up Spotify authentication and return a Spotify API client.

    Args:
        client_id (str): Spotify client ID.
        client_secret (str): Spotify client secret.ṇ

    Returns:
        spotipy.Spotify: A Spotify API client instance.
    """
    try:
        # Spotify client credentials manager
        client_credentials_manager = SpotifyClientCredentials(
            client_id="a6299ccf5c524261808903b130ca1919", client_secret="0f2f024b63754b3faf290976aeb05284"
        )

        # Creating Spotify API client
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        return sp

    except Exception as e:
        print("Error:", e)
        return None
