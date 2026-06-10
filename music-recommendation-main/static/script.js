// Function to fetch songs based on the selected artist
function fetchSongsByArtist(artist) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var songs = JSON.parse(xhr.responseText);
        var songSelect = document.getElementById("songSelect");
        // Clear existing options
        songSelect.innerHTML = "<option value=''>Select the song</option>";
        // Add new options
        songs.sort();

        songs.forEach(function (song) {
          var option = document.createElement("option");
          option.value = song;
          option.textContent = song;
          songSelect.appendChild(option);
        });
      } else {
        console.log("Error fetching songs from server.");
      }
    }
  };
  // Construct the request URL
  var url = "/get_songs?artist=" + artist;
  // Open the AJAX request
  xhr.open("GET", url, true);
  xhr.send();
}

// Add an event listener to the #artistSelect dropdown
document.getElementById("artistSelect").addEventListener("change", function () {
  var artist = this.value;
  // Check if an artist is selected
  if (artist) {
    // Fetch songs of the selected artist
    fetchSongsByArtist(artist);
  } else {
    // Clear options of #songSelect dropdown if no artist is selected
    document.getElementById("songSelect").innerHTML =
      "<option value=''>Select the song</option>";
  }
});

// Function to render a song card
function render(item) {
  return `
    <div class="song-card">
      <img src="${item.image_url}" alt="${item.song_name}">
      <a class="icon-link" href="${item.spotify_url}" target="_blank">
        <i class="fa-solid fa-headphones"></i>
      </a>
      <div class="info">
        <h3>${item.song_name}</h3>
        <h5>${item.artist}</h5>
      </div>
    </div>`;
}

// Function to perform the search
function recommend() {
  // Display the loading indicator
  document.getElementById("loading").style.display = "flex";

  var artist = document.getElementById("artistSelect").value;
  var song = document.getElementById("songSelect").value;

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      // Hide the loading indicator
      document.getElementById("loading").style.display = "none";

      if (xhr.status === 200) {
        var responseArray = JSON.parse(xhr.responseText);
        // Clear existing music cards
        var songCardsContainer = document.querySelector(".song-cards");
        songCardsContainer.innerHTML = "";
        // Iterate over the results and add new music cards
        responseArray.forEach(function (item) {
          songCardsContainer.innerHTML += render(item);
        });
      } else {
        console.log("Error processing request.");
      }
    }
  };
  // Construct the request URL
  var url = "/search?q=" + encodeURIComponent(artist + " - " + song);
  // Open the AJAX request
  xhr.open("GET", url, true);
  xhr.send();
}
