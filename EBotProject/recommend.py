import os
from dotenv import load_dotenv,find_dotenv
import requests
toneWithTagMap={
    'Joy':'joy',
    'Sadness':'motivational',
    'Analytical':'instrumental',
    'Anger':'chillout',
    'Fear':'motivational',
    'Confident':'rock',
    'Tentative':'acoustic',
    'Neutral':'experimental',
    " ":"rock"
}
load_dotenv(find_dotenv())
def recommendsongs(tone="Neutral"):
    i=1
    d={}
    tag=toneWithTagMap[tone]
    params={
        'api_key':os.environ.get("API_KEY"),
        'limit':5,
        'method':'tag.getTopTracks',
        'tag':tag,
        'format':'json'
         }
    res = requests.post('http://ws.audioscrobbler.com/2.0', params=params)
    songs={}
    for val in res.json()['tracks']['track']:
        songs[val['name']]=[val['url'],val['artist']['name']]
 
    for key in songs:
        d["song"+str(i)]=key
        d["link"+str(i)]=songs[key][0]
        i+=1
    d["rec"]=1
    return d
  


    