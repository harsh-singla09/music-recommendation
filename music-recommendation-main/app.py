import os

from flask import Flask, render_template, request, jsonify
from functions.utils import preprocess_data, dropbox_values
from functions.clustering_music import clustering_music_projection
from spotify.recommendations import recommend_id, recommend_music

from datetime import datetime

app = Flask(__name__)

data = preprocess_data("data/all_data.csv")

projection, _, _, _ = clustering_music_projection(data)


@app.route("/")
def index():
    year = datetime.today().year
    artists, songs = dropbox_values(data)
    return render_template("index.html", artists=artists, songs=songs, year=year)


@app.route("/search")
def recommend_music_route():
    # Obter os parâmetros da consulta da solicitação GET
    artist_song = request.args.get("q")

    # Chama a função que gera as recomendações e obtenha os dados necessários
    playlst_id = recommend_music(artist_song, projection, data)["id"]
    song_names, image_urls, artist, spotify_url = recommend_id(playlst_id)

    music_data = []
    for name, url, artist, spotify_url in zip(
        song_names, image_urls, artist, spotify_url
    ):
        music_data.append(
            {
                "song_name": name,
                "image_url": url,
                "artist": artist,
                "spotify_url": spotify_url,
            }
        )

    return jsonify(music_data)


@app.route("/get_songs")
def get_songs_by_artist():
    artist = request.args.get("artist")
    songs = data[data["artists"] == artist]["name"].unique().tolist()
    return jsonify(songs)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
