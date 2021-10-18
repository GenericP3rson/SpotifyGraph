# Spotify Graph
Graph of songs, artists, albums, and playlists from Spotify

## Prerequsities

* [pyTigerGraph](https://pypi.org/project/pyTigerGraph/)
* [Kaggle](https://pypi.org/project/kaggle/) (if installing from the API)

## Quick Set Up

1. [Get Started with TigerGraph Cloud](https://developers.tigergraph.com/quickstart)
2. Create an account on [Kaggle](https://kaggle.com/) (if directly importing data from kaggle).
3. Run `SpotifyGraph.ipynb`, replacing it with the appropriate credentials.

## Breakdown

### Data
The data is from the [Kaggle Spotify Dataset](https://www.kaggle.com/siropo/spotify-multigenre-playlists-data).

### EDA

- Adds a "Track Name" column with the genre

### Scripts

#### Schema
![Schema](https://media.discordapp.net/attachments/691840155325038592/899685971677831188/Screen_Shot_2021-10-18_at_10.50.47_AM.png?width=2328&height=1354)

#### Loads
None, see `SpotifyGraph.ipynb`

#### Query
There are a few queries to grab data for analysis, including:

1. `getArtists.gsql` —> Grabs all of the Artist vertices.
2. `getGenres.gsql` –> Grabs all of the Genre vetices.
3. `getPlaylists.gsql` —> Grabs all of the Playlist vertices.
4. `getSongs.gsql` —> Grabs all of the Song vertices.
5. `getSongsByArtists.gsql` –> Grabs songs by artist. 
6. `getSongsByGenre.gsql` —> Grabs songs by genre. 
7. `getSongsByPlaylist.gsql` —> Grabs songs by playlist.
8. `getVerticesFromSongs.gsql` —> Grabs genre, playlist, and artist by song.

## Projects

`TigerGraph_and_Cytoscape.ipynb` —> Lab of creating an interactive Cytoscape dashboard with Plotly's Cytoscape and the TigerGraph Spotify Graph.

## External Links

* [Spotify Graph Dashboard (Part I): Creating a Spotify Graph with TigerGraph](https://shreya-chaudhary.medium.com/spotify-graph-dashboard-part-i-creating-a-spotify-graph-with-tigergraph-af97c436e538?sk=0c2070552bbac70eeae351fc2b1e0630)
* [Spotify Graph Dashboard (Part II): Creating an Interactive Python Dashboard with Streamlit using TigerGraph Spotify Data](https://shreya-chaudhary.medium.com/spotify-graph-dashboard-part-ii-creating-an-interactive-python-dashboard-with-streamlit-using-17b737310042?sk=4b6fae139bac53e96c1427c836161ea8)
* [Modeling TigerGraph Spotify Data with Cytoscape](https://towardsdatascience.com/modelling-tigergraph-spotify-data-with-cytoscape-9b82ea614bed?sk=4d442dbb0a79e4b7b3d3b3b20c8a1f98)
