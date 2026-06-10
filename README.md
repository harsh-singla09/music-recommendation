# Music Recommendation System

This project is a web application built with Flask that recommends music based on user preferences. It utilizes machine learning techniques for music clustering and the Spotify API for fetching detailed information about recommended songs.

![music_recommendation_website](https://github.com/user-attachments/assets/95dc1bcb-e72b-4b47-a635-c2fb89e0a15a)

## Features

1. Music Recommendation: Users can select their favorite artist and song to receive personalized music recommendations based on their musical taste.
2. Advanced Machine Learning: The recommendations are generated using advanced machine learning techniques. The algorithm analyzes various factors such as valence, acousticness, danceability, energy, liveness, and speechiness of the music.
3. Spotify Integration: Detailed information about recommended songs, including the song name, artist name, Spotify URL, and album image, is fetched using the Spotify API.
4. User-Friendly Interface: The application provides a user-friendly interface for easy navigation and interaction.

## How It Works

1. Select Artist and Song: Users choose their favorite artist and song from the provided dropdown menus.
2. Fetch Recommendations: Upon clicking the "Pesquisar" button, the application sends an AJAX request to the server to fetch music recommendations based on the selected artist and song.
3. Display Recommendations: The server processes the request, generates recommendations using machine learning, and sends back a JSON response containing information about recommended songs.
4. Show Recommendations: The application dynamically renders music cards displaying the recommended songs' details, including song name, artist, and album image.

## Prerequisites

Before running this project, ensure that you have the following prerequisites installed:

- Python 3.x
- Python libraries: pandas, scikit-learn, spotipy, plotly, matplotlib, scikit-image
- Spotify Developer Account

### Spotify Configuration

You'll also need Spotify credentials for authentication. Follow the steps below to set up your credentials:

1. Access [Spotify for Developers](https://developer.spotify.com/dashboard/) and log in or create an account.
2. Create an app in the Spotify Dashboard and obtain your Client ID and Client Secret.
3. Create a `.env` file in the root directory of your project with the following content:

   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   ```

## Project Structure

The project structure is organized as follows:

- **app.py**: Contains the Flask application and routes for handling requests.
- **functions/**: Directory containing utility functions for data preprocessing and music clustering.
- **spotify/**: Directory containing functions for interacting with the Spotify API.
- **templates/**: Directory containing HTML templates for rendering pages.
- **static/**: Directory containing static files such as CSS stylesheets and JavaScript scripts.
- **data/**: Contains CSV files with Spotify data.

## Features

This project offers the following features:

- Data Preprocessing
- Visualization
- Spotify Authentication
- Music Recommendation
- Clustering

## Usage

To use this music recommendation system, follow the instructions below:

1. Clone this repository to your local environment:

```bash
git clone https://github.com/christianduhp/music-recommendation.git
```

2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Configure your Spotify credentials in the .env file:

Replace `your_client_id`, `your_client_secret`, and `your_redirect_uri` with your actual Spotify client ID, client secret, and redirect URI, respectively.

Run the main.py file to start the web application:

```bash
python app.py
```

5. Access the web application in your browser at http://localhost:5000.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
