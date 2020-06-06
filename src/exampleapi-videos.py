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
DEVELOPER_KEY = "AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis"

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
    f = open('playlist2', "r")
    lines = f.readlines()
    f.close()

    full_commennts = set()

    for i in ["DSid3SudPoA", "az3oo4wHnXY", "w_qiJSHUGnc", "n56U6FMK6Xg", "SfZHGtTGRn0", "6uyclhNWN5E", "LMytn90uAS8", "OFf66RbtiXs", "t5-pHGyTFjI", "9NcTW3jdm1M", "WCQTxnNuKe0", "guMUksv4fO8", "t2NF4YIOp18", "2kH94N4CdBs", "C1k1qpRlnxU", "XJy-5aLjhZY", "K8VQ9dFHJb4", "xgapWF1fpfs", "01eO9INWmS4", "njrLdKL3kbs", "oUyEw3h-TN0", "CAPX0AMbxZE", "w8fvgujrKi4", "aXNwdOWIc8s", "V_UNSRN9IdQ", "a77pe3ZstCM", "qjHPy8n8JOY", "aghOyBpo9Kg", "QliKBmWieAY", "MJUb13KLEx4", "AVFA78j7yag", "GkEpYhlFer4", "JdV-ZsKAdjs", "VD-K63YxHbQ", "qbzvw_dzbjs", "1mQeALggCXs", "gHzP7U_cXi4", "9dCBsqpsVOI", "l9QDhLKsXt0", "FyiK_ZmxkZk", "FjVKDFHFDns", "OfxpkQ379ms", "tVAbPcHIG6o", "txiXprSGlYw", "-6NQ6Fut8Qw", "Eml4Cw4VQ1w", "6JQPQIdAGqs", "1jFQ_1eflTI", "qRTVCBeyplI", "tT6K-Gz1Uhs", "P33kiIHcu44", "Zfvr4piQdms", "6f2en1O-IvM", "8jgFb3e6NGc", "QHYqsukgpXU", "A3_zHm3-2-k", "PuYonApyhGA", "DmDyhIlNy2Y", "5v_mjxYhrJI", "QQg8DqHI-H4", "AZ5KdxjrPow", "74sDoUdqJps", "2ler9MzN5KY", "1AHX8kxfLkQ", "Xh-jeMj3Kjs", "3W18DQCDxwc", "tueTPWPLPNs", "YEr4A0zeaWQ", "cegGDh90Ltw", "io1ll_OgxRw", "B96XZr2s7u4", "T3RoaLpeg3g", "nFHr4jOdVxY", "yDe8e_QVRQU", "KOqCnvz9HPk", "O1anDJJnslc", "LDyKvnhOgWU", "Ps3xIhhJz8U", "kEG-42dk8X0", "uYTYqG1Z0SQ", "qq2oLyHMqVM", "lJOgp6hRaAg", "-BqYSIBkE2Y", "W9H3AmfTons", "2mLAFBWtC4o", "PJrOiU6VlfU", "i3mg6sUpEII", "kbsaPanbSuA", "NQDCSAtIdhQ", "t2foHEwSSRg", "5iWCQVXc7ao", "LkSgmfRiYn8", "F_N12cimQuc", "Rn-2tMOXQX8", "wMRa27hnbHc", "gZQoll091dk", "BnSjP3F_0Zo", "4G9bXKWjblg", "y1koV9TkjPs", "wdHbEA-nxRc", "CfB8LND752A", "b2s1itdXnGY", "gezU_zLYDw0", "M96e02ZG1QM", "_ConUtxHwMY", "MvICaNbEaW8", "5MabRx71j4g", "SpZVugvanCg", "zyfxuvzcBPE", "N6EujK5-tV0", "0cyU_vBaXL8", "c51fXrfHaXM", "fHjUtGPENM8", "O3A5rpDJGPg", "3vTFS7LQOC8", "myCiSfdiK-A", "PJdGDFpQILo", "mhtr5WkjRGs", "NzyAcjY_NFE", "BoRi_pgFrl0", "v-ZfOCMBEuI", "B8TH4nl0U6s", "yXqhhm3Z6vI", "lqL-m8gawAc", "2q7sWktM8kw", "BLxiuJVAFyY", "khOxP-HwdgM", "xWOVEf87WGw", "dQjhL7w7EyI", "tnR-U6fiCwo", "bMpu8emmSa0", "6_I51AIjkhg", "ARrHMgUEu44", "XRnL8qTMYHc", "SLnT4TlOJis", "CBtIYcP6ijk", "V0PpS0INbyI", "h2bviMr5M_o", "K_LbKneIk6k", "opxCee2uwL0", "uilxJH6J3aM", "1GXjj0bCNXY", "7kxudgCfg6g", "b26wW8uko8U", "4NetayLahTs", "6HtdmMdJjc4", "8fZuN-r5FVU", "6nyor9Gx8ig", "rWgnmKPZ-nA", "jNfFffnAGHU", "4_WeDyLh_ag", "g1MUsT9UjrY", "Iv-5jYmu60o", "DbNWpKGqavo", "ZDjt4gT_-jA", "XWVM6T4vG7Q", "0AAwca-miu0", "p-wlzt--Gv8", "dsgtlsy2UvE", "8cFXX-YaESc", "CLxr9YWJRBc", "NrxONRkX9oY", "pfQ8EH735ro", "Wlh9yG2MKFc", "oCgRSHGIXmo", "5GZiJV8ABHs", "DoNytxLWrKs", "Ez9BvOt2whA", "D-l-FHwfmmI", "Eyk6glmCTE4", "1t09iLF7BYQ", "93HWw15yzEA", "Ay0fEdbNM5o", "oishdvTKtoo", "1dHVQytQF3E", "O_zkowOXemY", "H9anqyrK7NA", "wvSh-mOGQhY", "8FzDYtpWzfg", "7MJ3HBzDxWE", "UsQFtX4rtbc", "XA7HDr1Nw78", "ijDAyFTorlQ", "hmSIz4DQv10", "haxoVEN7T9g", "FEsgm5IurP8", "3Kjl7oo7zC8", "auV5b0cWV9I", "mNK22Vwhri8", "n-vtzBaBL44", "hAk_tkjHjt4", "Qa1kmGYcL6U", "M02xhdIRHCE", "5ZBVDbE4s5g", "-eYLjOGgP4c", "Ntzz4WMJoN8", "4Mkg5SbO1kw", "ISL6-ruD-jo", "ypgtobb08E0", "HekKqOZCxNo", "fHDNQTBkeRA", "PO-0Wdh7p1o", "GaMP2BmOXp0", "Ui6TYItprvY", "aIIqoXp52V0", "9X_sBOTyhjw", "hJNiHdv29Yg", "w8NtDGFj1c8", "YLpiCMynqkA", "awL-XpFQoQ8", "vDbz4AjLh40", "kl0sqA_c9RY", "f_ZFGIaAQRo", "9B3wH4YNQ4w", "VkQaWGaLTwM", "WDKLJlM3StQ"]:
        set.add(get_comments(i))