# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python




import os

import json

import googleapiclient.discovery

import google_auth_oauthlib.flow

import googleapiclient.errors


import requests



palavras_chave = ["terra plana", "terraplanismo", "globo", "globismo", "terraplanistas", "conspiracao", "conspiração", "conspiraçao", "plana", "plano", "ideologia"]



os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyAauHYQ-rEzrHlcLojAl8-pQHdiDjVrVQg"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)



def get_comments(id, filter__=False):
    erros = []

    print(f"Getting video {id}")

    r =requests.get(f'https://www.youtube.com/watch?v={id}')
    aa = r.text.lower()
    result = 0
    for i in palavras_chave:
        result+=aa.find(i)
    if result<0 and filter__:
        return None

    comments = set()
    videos = set()
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=id,
        maxResults=50
    )
    response = request.execute()

    snippets = [i['snippet']['topLevelComment']['snippet'] for i in response['items']]
   
    for i in snippets:
        try:
            videos.add(i['authorChannelUrl'] + ":" + i['textDisplay'])
            #comments.add()
        except KeyError:
            erros.append(i)
            
    try:
        nextPageToken = response['nextPageToken']
    except KeyError:
        return videos

    while (1):
        request = youtube.commentThreads().list(
       part="snippet",
        videoId=id,
        maxResults=50,
        pageToken=nextPageToken
        )
        try:
            nextPageToken = response['nextPageToken']
        except KeyError:
            break
        response = request.execute()
        for i in snippets:
            try:
                videos.add(i['authorChannelUrl'] + ":" + i['textDisplay'])
            except KeyError:
                erros.append(i)
    print(len(erros))
    return videos

    

def get_all_coments_from_playlist(id, filter__=False):
    print(f"Start {id}")
    videos = get_playlist_itens(id)
    ii = []
    for i in videos:
        try:
            aa = get_comments(i, filter__)
            ii += aa
        except Exception as e:
            print(e)
            with open(id.replace("\n", ""), "a") as ff:
                json.dump(ii, ff)
        
    with open(id.replace("\n", ""), "a") as ff:
        json.dump(ii, ff)

    print(f"Done {id}")

    


def get_playlists(id='UCv29ytb-v_Ph6QZOypGFyEw'):

    request = youtube.channels().list(
        part="contentDetails",
        id=id,
        maxResults=50
    )
    response = request.execute()

    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


def get_playlist_itens(id):
    videos = set()
    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=50,
        playlistId=id
    )
    response = request.execute()
    [videos.add(i) for i in [i['contentDetails']['videoId'] for i in response['items']]]
    try:
        nextPageToken = response['nextPageToken']
    except KeyError:
        return videos
    while (1):
        request = youtube.playlistItems().list(
            part="contentDetails",
            maxResults=50,
            playlistId=id,
            pageToken=nextPageToken
    
        )
        try:
            nextPageToken = response['nextPageToken']
        except KeyError:
            break
        response = request.execute()
        [videos.add(i) for i in [i['contentDetails']['videoId'] for i in response['items']]]
    return videos


def go():
    data = None
    with open('channels.json') as json_file:
        data = json.load(json_file)

    uploads = []
    for i in data['channels']["type"]["id"]:
        print(i)
        uploads.append(get_playlists(i))
    videos = []

    print(1)
    for i in uploads:
        print(i)
        videos +=(list(get_playlist_itens(i)))
    print(2)
    print(videos)

    comments = []

    print(list(videos))

    for i in list(videos):
        
        comments+= get_comments(i)

    print(comments)
    with open("teste", "w") as ff:
        json.dump(comments, ff)




def getAllComentsPerChannel(id = "UC6IYj9pQ5sv6zqZrISZNRzQ"):
    rep = []
    request = youtube.commentThreads().list(
        part="snippet",
        allThreadsRelatedToChannelId= id
    )
    response = request.execute()
    rep += [[i['snippet']['topLevelComment']['snippet']['channelId'], i['snippet']['topLevelComment']['snippet']['textOriginal']] for i in response['items']]
    try:
        nextPageToken = response['nextPageToken']
    except KeyError:
        print(rep)
        return rep
    

    while (1):
        request = youtube.playlistItems().list(
            part="contentDetails",
            maxResults=50,
            playlistId=id,
            pageToken=nextPageToken
    
        )
        try:
            nextPageToken = response['nextPageToken']
        except KeyError:
            break
        response = request.execute()
        rep += [[i['snippet']['topLevelComment']['snippet']['channelId'], i['snippet']['topLevelComment']['snippet']['textOriginal']] for i in response['items']]
        f = open(id, "a")
        f.write(",".join(rep))
        f.close()

    return rep
    


    return (response)

#print(getAllComentsPerChannel()) # 3 unidades - 50 comentarios (10.000) = 166650 comentarios por rodada

if __name__ == "__main__":
#    f = open('playlist2', "r")
#    lines = f.readlines()
#    f.close()

#    full_commennts = set()

#    for i in [
#"7YwG8pnfSa8",
#"we0D78_skIA",
#"u2zUap1s2BE",
#"X8KGoLBsKok",
#"6rgSdb90Ykg",
#"GPIfYwgjowI",
#"JD0jHSeGEps",
#"SycYVU1Ikp4",
#"aW-qbx04gS4",
#"brQf3avYAEo",
#"DB8yS16aVAs",
#"EDhMWvVHZ5Y",
#"TsGnRdj8vzI"]:
# TsGnRdj8vzI
     with open(f"M-TsGnRdj8vzI", "w") as ff:
          json.dump(list(get_comments("TsGnRdj8vzI")), ff)
        
        
        
        
        
