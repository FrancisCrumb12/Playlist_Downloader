# Playlist Downloader


A simple command-line tool to download the audio from all videos in a YouTube playlist. The script organizes the downloaded audio files into a specified folder within your system's default Music directory.

## Features

*   Downloads audio-only streams from YouTube playlist videos.
*   Prompts the user to create a new folder for each playlist download.
*   Saves downloaded files to a default Music directory (`C:\Users\<USERNAME>\Music\` on Windows, `usr/share/Music/` on other systems).
*   Validates YouTube playlist URLs.
*   Simple and interactive command-line interface.

## Prerequisites

*   Python 3.x
*   pip

## Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/franciscrumb12/playlist_downloader.git
    cd playlist_downloader
    ```

2.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  Run the script from your terminal:
    ```sh
    python main.py
    ```

2.  When prompted, enter a name for the folder where the audio files will be saved. This folder will be created in your system's Music directory.
    ```
    What do you want to name this folder?
    > My Awesome Playlist
    ```

3.  Next, paste the full URL of the YouTube playlist you want to download and press Enter.
    ```
    Enter the link of the playlist you wish to download.
    > https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxx
    ```

4.  The script will then begin downloading the audio track from each video in the playlist. The progress will be displayed in the console.

    ```
    Downloading playlist: "Playlist Title"
    Downloading: Video Title 1
    Downloading: Video Title 2
    ...
    Download completed at: C:\Users\YourUser\Music\My Awesome Playlist
    ```

The downloaded audio files will be located in the folder you created inside your Music directory.
