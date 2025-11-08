import os
import sys
from pytubefix import Playlist
from urllib.parse import urlparse

t = """    ____        __    _      __
   / __ \__  __/ /   (_)____/ /_
  / /_/ / / / / /   / / ___/ __/
 / ____/ /_/ / /___/ (__  ) /_
/_/    \__, /_____/_/____/\__/
      /____/        ver 0.1
"""

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
        print(t)

    else:
        os.system('clear')
        print(t)


def download_playlist(link, dest_path):
    while True:
        try:
            clear_screen()
            playlist = Playlist(link)
            print(f'Downloading playlist: "{playlist.title}"')

            for video in playlist.videos:
                ys = video.streams.get_audio_only()
                print(f'Downloading: {video.title}')
                ys.download(output_path=dest_path)

            print(f'Download completed at: {dest_path}')
            sys.exit(0)

        except Exception as e:
            print(f'Exception: {e} occurred!')

def validate_url(user_input):
    try:
        res = urlparse(user_input)

        if res.scheme and res.netloc:
            return True
        else:
            print("Not a valid url!")
    except Exception:
        return False

def main():

    folder = ''
    print(t)

    if os.name ==  'nt':
        USER = os.environ.get("USERNAME")  # GETS USER NAME
        PATH = f'C:\\Users\\{USER}\\Music\\' # DIRECTORY PATH

    else:
        PATH = 'usr/share/Music/'

    while True:
        try:
            clear_screen()

            folder = input('What do you want to name this folder?\n> ')
            dir = os.path.join(PATH, folder)
            os.mkdir(dir)

            clear_screen()
            print(f'Folder: {folder} Created at: {dir}')

            while True:
                try:
                    url = input('Enter the link of the playlist you wish to download.\n> ')
                    if validate_url(url):
                        download_playlist(url, dir)

                except Exception as e:
                    print(f'Exception {e} Occurred!')

        except FileExistsError:
            clear_screen()
            dir = os.path.join(PATH, folder)
            print('File already exists! Skipping...')

            while True:
                try:
                    url = input('Enter the link of the playlist you wish to download.\n> ')
                    if validate_url(url):
                        download_playlist(url, dir)

                except Exception:
                    print(f'Exception {e} Occurred!')
                    sys.exit(1)

        except OSError as e:
            print(f'Error creating file! : Error {e} Occurred!')
            sys.exit(1)

        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)


if __name__=='__main__':
    main()