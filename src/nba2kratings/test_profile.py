from bs4.element import PreformattedString
import pytest
from bs4 import BeautifulSoup
from nba_api.stats.static import players
from player_profile import Profile


@pytest.fixture
def player_profile():
    p = Profile()
    return p

def test_profile_200(player_profile): #Test valid response for valid name
    player_profile.get_player_info('Lebron James')
    print(player_profile._)
    assert player_profile.player_valid == True

def test_valid_profile(player_profile):
    player_profile.get_player_info('Lebron James')
    print(player_profile._)
    assert len(player_profile._) > 1

def test_profile_404(player_profile):
    player_profile.get_player_info('Lebr James')
    print(player_profile._)
    assert player_profile.player_valid == False

