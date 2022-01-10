import pandas as pd
import requests
import re
import json

from bs4 import BeautifulSoup
from nba_api.stats.static import players


base_url = "https://2kratings.com/{}"


def get_ratings(player_name):


    attr_dict = {}

    url_name = player_name.replace(' ', '-') #Replace spaces in name with hyphens

    #Retrieve html content for player
    r = requests.get(base_url.format(url_name))
    soup = BeautifulSoup(r.content, 'html.parser')


    #Return an empty dict if player not found
    if not soup.find('title'):
        print("Could not find ", player_name)
        return {}

    #Get Player Ratings
    ratings = {}
    labels = ["Overall", "Inside Scoring", "Outside Scoring", "Athleticism", "Playmaking", "Rebounding", "Defending"]
    scripts = soup.findAll('script')

    s = ''
    for x in scripts:
        
        if 'chartjs-radar' in x.get_text():
            s = x.get_text()
            break
    
    if len(s) > 0:
        m = re.search(r"\[([\d,\s]+)\]", s)
        scores = [int(x) for x in m.group(1).split(',') if x != '']
        ratings = dict(zip(labels, scores))


    return ratings