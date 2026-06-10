import os
from sklearn.metrics.pairwise import euclidean_distances
from spotify.auth import setup_spotify_authentication as sp

spotify_client_id = os.environ.get("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

spotify = sp(spotify_client_id, spotify_client_secret)


def recommend_id(playlist_id):
    """
    Get track information for a list of playlist IDs.

    This function retrieves track details including album images, track names,
    artist names, and Spotify URLs for a list of playlist IDs.

    Args:
        playlist_id (list): A list of playlist IDs.

    Returns:
        tuple: A tuple containing four lists - track names, album image URLs,
        artist names, and Spotify URLs.
    """

    image_url = []
    name = []
    artist = []
    spotify_url = []

    for i in playlist_id:
        # Retrieve track information from Spotify
        track = spotify.track(i)

        image_url.append(track["album"]["images"][1]["url"])
        name.append(track["name"])
        artist.append(track["album"]["artists"][0]["name"])
        spotify_url.append(track["external_urls"]["spotify"])

    return name, image_url, artist, spotify_url


def recommend_music(input_song, projection_data, music_data):
    """
    Recommends music based on the similarity to an input song.

    Args:
        input_song (str): The name of the input song.
        projection_data (DataFrame): The DataFrame containing song projections.
        music_data (DataFrame): The DataFrame containing music data.

    Returns:
        recommended_music (DataFrame): A DataFrame with recommended music based on similarity.
    """
    # Find the cluster of the input song
    input_song_cluster = projection_data[projection_data["song"] == input_song][
        "cluster_pca"
    ].values[0]

    # Filter music in the same cluster
    music_in_cluster = projection_data[
        projection_data["cluster_pca"] == input_song_cluster
    ][[0, 1, "song"]]

    # Find the coordinates of the input song
    input_song_x = projection_data[projection_data["song"] == input_song][0].values[0]
    input_song_y = projection_data[projection_data["song"] == input_song][1].values[0]

    # Calculate Euclidean distances between input song and others in the cluster
    distances = euclidean_distances(
        music_in_cluster[[0, 1]], [[input_song_x, input_song_y]]
    )

    # Add id to the recommended_music DataFrame
    music_in_cluster["id"] = music_data["id"]

    # Add distances to the DataFrame
    music_in_cluster["distances"] = distances

    # Sort by distances and select the top 10 recommendations
    recommended_music = music_in_cluster.sort_values("distances").head(10)
    return recommended_music
