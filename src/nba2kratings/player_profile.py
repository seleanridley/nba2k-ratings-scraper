import requests

from bs4 import BeautifulSoup 
from nba_api.stats.static import players


base_url = "https://2kratings.com/{}"

class Profile():

    def __init__(self):
        self.player_valid = None
        self._ = {}
        self.player_image = ''

    
    def __is_player_valid(self, player_name):
        url_name = player_name.replace(' ', '-')
            
        r = requests.get(base_url.format(url_name))
        soup = BeautifulSoup(r.content, 'html.parser')
        
        if soup.find('title').string == 'Page not found - 2K Ratings':
            print("Could not find ", player_name)
            self.player_valid = False
        else:
            self.player_valid = True

        return soup


    def get_player_info(self, player_name):

        soup = self.__is_player_valid(player_name)
        
        if not self.player_valid:
            return {}
        else:
            #Get Player Info
            info_dict = {}
            info_labels = ['Team', 'Archetype', 'Position', 'Jersey']
            info = soup.find('div', {"class": "player-info"})
            if info:
                player_i = info.findAll('p', {"class": 'mb-0'})
                p_list = [x.get_text(strip=True).split(':') for x in player_i][1:]
                info_dict = {p[0]: p[1].strip() for p in p_list if p[0] in info_labels}
                self._ = info_dict
        

    def get_player_image(self, player_name):
        
        self.__is_player_valid(player_name)
     
        if not self.player_valid:
            return {}
        else:
            #Get Player Image
            id = players.find_players_by_full_name(player_name) 
            if id:
                id = id[0]['id']
                img_url = "https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{}.png".format(id)
                self.player_image = img_url
           

    

