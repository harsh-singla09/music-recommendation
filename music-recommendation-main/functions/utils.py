import pandas as pd

def load_data(data):
    data = pd.read_csv(data)
    return data

def preprocess_data(data):
    data = load_data(data)
    data = data.drop(["explicit", "key", "mode"], axis=1)
    return data

def preprocess_data_by_genres(data):
    data = load_data(data)
    data = data.drop(["key", "mode"], axis=1)
    return data

def preprocess_data_by_years(data):
    data = load_data(data)
    data = data[data["year"] >= 2000]
    data = data.drop(["key", "mode"], axis=1)
    data.reset_index
    return data

def dropbox_values(df):
    artists = sorted(df["artists"].unique())
    songs = sorted(df["name"].unique())
    return artists, songs
