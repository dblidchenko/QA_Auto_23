import pytest
from modules.api.clients.discogs import Discogs


@pytest.mark.api
def test_get_artist(discogs_api):
    r = discogs_api.get_artist('695689')
    assert r['name'] == 'Svreca'


@pytest.mark.api
def test_get_not_existing_artist(discogs_api):
    r = discogs_api.get_artist('dblidchenko')
    assert r['message'] == 'The requested resource was not found.'


@pytest.mark.api
def test_get_label(discogs_api):
    r = discogs_api.get_label('93202')
    assert r['name'] == 'Dais Records'


@pytest.mark.api
def test_remove_artist(discogs_api):
    r = discogs_api.delete_artist('695689')
    assert r['message'] == 'Method DELETE is not allowed for this resource.'
