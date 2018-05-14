import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_MOVIE_UP = os.path.join(BASE_DIR, 'upload_movie')
BASE_MOVIE_DOWN = os.path.join(BASE_DIR, 'download_movie')

server_address = ('127.0.0.1', 8087)
