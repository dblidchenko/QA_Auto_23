import requests


class Discogs:

    def get_label(self, label_id):
        r = requests.get(f'https://api.discogs.com//labels/{label_id}')
        body = r.json()

        return body

    def get_artist(self, artist_id):
        r = requests.get(f'https://api.discogs.com/artists/{artist_id}')
        body = r.json()

        return body

    def delete_artist(self, artist_id):
        r = requests.delete(f'https://api.discogs.com/artists/{artist_id}')
        body = r.json()

        return body
