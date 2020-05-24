# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python




import os

import json

import googleapiclient.discovery

import google_auth_oauthlib.flow

import googleapiclient.errors



os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"


youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)



def get_comments(id):
    erros = []

    print(id)
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
            comments.add()
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
    return videos

    

def get_all_coments_from_playlist(id):
    videos = get_playlist_itens(id)
    ii = []
    for i in videos:
        try:
            aa = get_comments(i)
            ii += aa
        except Exception as e:
            with open(id, "a") as ff:
                json.dump(ii, ff)
        
    with open(id, "a") as ff:
        json.dump(ii, ff)

    


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