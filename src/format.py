import re
import json
pattern = re.compile("(video )([A-Za-z0-9_-]+)")
id = 'ateste'
clean = set()
print(1111)

text = '''
Getting video oishdvTKtoo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=oishdvTKtoo&maxResults=50&pageToken=QURTSl9pMDJBZDVXZDFzcU1obzBXREtFT2haM2dNQl9GcDRNaVlqeXlmbkZJNnExNFBpTjZ5QUFzS2N5d2ZiQVYyRGxvbFBvWkk1NUltbXJhVXYzV3daXzlsOF94Z2pmRUlNM2xTbnR0ZnUwOElKakNxWk5nVlFxX2pSbzRfeDBGZ1o2OUdjYnhNMFFTZ0E0TDRNVU94U2FjNjlnTEN1cGhVTDRrZ05zVGI5dFhTdUIzdw%3D%3D&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video T3RoaLpeg3g
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=T3RoaLpeg3g&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video XRnL8qTMYHc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=XRnL8qTMYHc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 7MJ3HBzDxWE
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=7MJ3HBzDxWE&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video y1koV9TkjPs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=y1koV9TkjPs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Ez9BvOt2whA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Ez9BvOt2whA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video xgapWF1fpfs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=xgapWF1fpfs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 3Kjl7oo7zC8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=3Kjl7oo7zC8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video MvICaNbEaW8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=MvICaNbEaW8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video lJOgp6hRaAg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=lJOgp6hRaAg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video n56U6FMK6Xg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=n56U6FMK6Xg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video AZ5KdxjrPow
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=AZ5KdxjrPow&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Iv-5jYmu60o
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Iv-5jYmu60o&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video JdV-ZsKAdjs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=JdV-ZsKAdjs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 5iWCQVXc7ao
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=5iWCQVXc7ao&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Rn-2tMOXQX8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Rn-2tMOXQX8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video myCiSfdiK-A
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=myCiSfdiK-A&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video HekKqOZCxNo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=HekKqOZCxNo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video YEr4A0zeaWQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=YEr4A0zeaWQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 5MabRx71j4g
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=5MabRx71j4g&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video ARrHMgUEu44
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=ARrHMgUEu44&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video M96e02ZG1QM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=M96e02ZG1QM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video YLpiCMynqkA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=YLpiCMynqkA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video F_N12cimQuc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=F_N12cimQuc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video njrLdKL3kbs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=njrLdKL3kbs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video aghOyBpo9Kg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=aghOyBpo9Kg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video w8fvgujrKi4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=w8fvgujrKi4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video khOxP-HwdgM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=khOxP-HwdgM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video A3_zHm3-2-k
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=A3_zHm3-2-k&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video f_ZFGIaAQRo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=f_ZFGIaAQRo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video FEsgm5IurP8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=FEsgm5IurP8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video AVFA78j7yag
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=AVFA78j7yag&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video LkSgmfRiYn8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=LkSgmfRiYn8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 1dHVQytQF3E
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=1dHVQytQF3E&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Ui6TYItprvY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Ui6TYItprvY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video guMUksv4fO8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=guMUksv4fO8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video zyfxuvzcBPE
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=zyfxuvzcBPE&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 4_WeDyLh_ag
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=4_WeDyLh_ag&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video b2s1itdXnGY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=b2s1itdXnGY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video SpZVugvanCg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=SpZVugvanCg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video fHjUtGPENM8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=fHjUtGPENM8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video VkQaWGaLTwM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=VkQaWGaLTwM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video az3oo4wHnXY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=az3oo4wHnXY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video hAk_tkjHjt4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=hAk_tkjHjt4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 4G9bXKWjblg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=4G9bXKWjblg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 8cFXX-YaESc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=8cFXX-YaESc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video WCQTxnNuKe0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=WCQTxnNuKe0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video txiXprSGlYw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=txiXprSGlYw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video v-ZfOCMBEuI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=v-ZfOCMBEuI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 74sDoUdqJps
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=74sDoUdqJps&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video kbsaPanbSuA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=kbsaPanbSuA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video NrxONRkX9oY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=NrxONRkX9oY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video vDbz4AjLh40
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=vDbz4AjLh40&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video uilxJH6J3aM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=uilxJH6J3aM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video MJUb13KLEx4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=MJUb13KLEx4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video B96XZr2s7u4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=B96XZr2s7u4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video H9anqyrK7NA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=H9anqyrK7NA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video a77pe3ZstCM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=a77pe3ZstCM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video OFf66RbtiXs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=OFf66RbtiXs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video SfZHGtTGRn0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=SfZHGtTGRn0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video CfB8LND752A
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=CfB8LND752A&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 1t09iLF7BYQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=1t09iLF7BYQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video t2foHEwSSRg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=t2foHEwSSRg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video ISL6-ruD-jo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=ISL6-ruD-jo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video jNfFffnAGHU
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=jNfFffnAGHU&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video VD-K63YxHbQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=VD-K63YxHbQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 8fZuN-r5FVU
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=8fZuN-r5FVU&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video w8NtDGFj1c8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=w8NtDGFj1c8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 0AAwca-miu0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=0AAwca-miu0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video O1anDJJnslc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=O1anDJJnslc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video D-l-FHwfmmI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=D-l-FHwfmmI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video opxCee2uwL0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=opxCee2uwL0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video t5-pHGyTFjI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=t5-pHGyTFjI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video DSid3SudPoA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=DSid3SudPoA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video uYTYqG1Z0SQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=uYTYqG1Z0SQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video -6NQ6Fut8Qw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=-6NQ6Fut8Qw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video h2bviMr5M_o
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=h2bviMr5M_o&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video kl0sqA_c9RY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=kl0sqA_c9RY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video wMRa27hnbHc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=wMRa27hnbHc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video FyiK_ZmxkZk
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=FyiK_ZmxkZk&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Eyk6glmCTE4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Eyk6glmCTE4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video auV5b0cWV9I
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=auV5b0cWV9I&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 9dCBsqpsVOI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=9dCBsqpsVOI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video wdHbEA-nxRc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=wdHbEA-nxRc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 9B3wH4YNQ4w
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=9B3wH4YNQ4w&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 6f2en1O-IvM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=6f2en1O-IvM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video ijDAyFTorlQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=ijDAyFTorlQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video qjHPy8n8JOY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=qjHPy8n8JOY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video PJdGDFpQILo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=PJdGDFpQILo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 2ler9MzN5KY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=2ler9MzN5KY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video wvSh-mOGQhY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=wvSh-mOGQhY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video aIIqoXp52V0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=aIIqoXp52V0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video M02xhdIRHCE
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=M02xhdIRHCE&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video GkEpYhlFer4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=GkEpYhlFer4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video io1ll_OgxRw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=io1ll_OgxRw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video tnR-U6fiCwo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=tnR-U6fiCwo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video tVAbPcHIG6o
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=tVAbPcHIG6o&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video n-vtzBaBL44
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=n-vtzBaBL44&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video oUyEw3h-TN0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=oUyEw3h-TN0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video fHDNQTBkeRA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=fHDNQTBkeRA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 0cyU_vBaXL8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=0cyU_vBaXL8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video bMpu8emmSa0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=bMpu8emmSa0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video WDKLJlM3StQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=WDKLJlM3StQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Ntzz4WMJoN8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Ntzz4WMJoN8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video OfxpkQ379ms
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=OfxpkQ379ms&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video V0PpS0INbyI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=V0PpS0INbyI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video mNK22Vwhri8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=mNK22Vwhri8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video qRTVCBeyplI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=qRTVCBeyplI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Ay0fEdbNM5o
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Ay0fEdbNM5o&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 6uyclhNWN5E
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=6uyclhNWN5E&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 9X_sBOTyhjw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=9X_sBOTyhjw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video B8TH4nl0U6s
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=B8TH4nl0U6s&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 4Mkg5SbO1kw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=4Mkg5SbO1kw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video dsgtlsy2UvE
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=dsgtlsy2UvE&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video l9QDhLKsXt0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=l9QDhLKsXt0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video w_qiJSHUGnc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=w_qiJSHUGnc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video qbzvw_dzbjs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=qbzvw_dzbjs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video NQDCSAtIdhQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=NQDCSAtIdhQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video K_LbKneIk6k
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=K_LbKneIk6k&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video PuYonApyhGA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=PuYonApyhGA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 8jgFb3e6NGc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=8jgFb3e6NGc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video V_UNSRN9IdQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=V_UNSRN9IdQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video aXNwdOWIc8s
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=aXNwdOWIc8s&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video i3mg6sUpEII
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=i3mg6sUpEII&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video NzyAcjY_NFE
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=NzyAcjY_NFE&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video N6EujK5-tV0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=N6EujK5-tV0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 1AHX8kxfLkQ
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=1AHX8kxfLkQ&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video QliKBmWieAY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=QliKBmWieAY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video FjVKDFHFDns
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=FjVKDFHFDns&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video XA7HDr1Nw78
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=XA7HDr1Nw78&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video DmDyhIlNy2Y
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=DmDyhIlNy2Y&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video XWVM6T4vG7Q
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=XWVM6T4vG7Q&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video kEG-42dk8X0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=kEG-42dk8X0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video K8VQ9dFHJb4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=K8VQ9dFHJb4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 5GZiJV8ABHs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=5GZiJV8ABHs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Wlh9yG2MKFc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Wlh9yG2MKFc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video yDe8e_QVRQU
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=yDe8e_QVRQU&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 6HtdmMdJjc4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=6HtdmMdJjc4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video tueTPWPLPNs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=tueTPWPLPNs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video CLxr9YWJRBc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=CLxr9YWJRBc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video ypgtobb08E0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=ypgtobb08E0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 6_I51AIjkhg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=6_I51AIjkhg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video g1MUsT9UjrY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=g1MUsT9UjrY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video cegGDh90Ltw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=cegGDh90Ltw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video CAPX0AMbxZE
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=CAPX0AMbxZE&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video _ConUtxHwMY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=_ConUtxHwMY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 6nyor9Gx8ig
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=6nyor9Gx8ig&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 1GXjj0bCNXY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=1GXjj0bCNXY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video rWgnmKPZ-nA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=rWgnmKPZ-nA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video nFHr4jOdVxY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=nFHr4jOdVxY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video haxoVEN7T9g
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=haxoVEN7T9g&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video p-wlzt--Gv8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=p-wlzt--Gv8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video hmSIz4DQv10
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=hmSIz4DQv10&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video yXqhhm3Z6vI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=yXqhhm3Z6vI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video qq2oLyHMqVM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=qq2oLyHMqVM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Eml4Cw4VQ1w
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Eml4Cw4VQ1w&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 7kxudgCfg6g
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=7kxudgCfg6g&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 1mQeALggCXs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=1mQeALggCXs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video -eYLjOGgP4c
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=-eYLjOGgP4c&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 93HWw15yzEA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=93HWw15yzEA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 2mLAFBWtC4o
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=2mLAFBWtC4o&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video UsQFtX4rtbc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=UsQFtX4rtbc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Zfvr4piQdms
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Zfvr4piQdms&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video PO-0Wdh7p1o
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=PO-0Wdh7p1o&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video DoNytxLWrKs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=DoNytxLWrKs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Qa1kmGYcL6U
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Qa1kmGYcL6U&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video LMytn90uAS8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=LMytn90uAS8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Xh-jeMj3Kjs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Xh-jeMj3Kjs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video xWOVEf87WGw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=xWOVEf87WGw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 8FzDYtpWzfg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=8FzDYtpWzfg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video dQjhL7w7EyI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=dQjhL7w7EyI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 2q7sWktM8kw
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=2q7sWktM8kw&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video P33kiIHcu44
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=P33kiIHcu44&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video Ps3xIhhJz8U
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=Ps3xIhhJz8U&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video BLxiuJVAFyY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=BLxiuJVAFyY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video SLnT4TlOJis
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=SLnT4TlOJis&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 5ZBVDbE4s5g
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=5ZBVDbE4s5g&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video oCgRSHGIXmo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=oCgRSHGIXmo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 5v_mjxYhrJI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=5v_mjxYhrJI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video C1k1qpRlnxU
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=C1k1qpRlnxU&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video KOqCnvz9HPk
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=KOqCnvz9HPk&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 2kH94N4CdBs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=2kH94N4CdBs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video CBtIYcP6ijk
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=CBtIYcP6ijk&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video -BqYSIBkE2Y
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=-BqYSIBkE2Y&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video lqL-m8gawAc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=lqL-m8gawAc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 01eO9INWmS4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=01eO9INWmS4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 4NetayLahTs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=4NetayLahTs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video PJrOiU6VlfU
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=PJrOiU6VlfU&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video XJy-5aLjhZY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=XJy-5aLjhZY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video hJNiHdv29Yg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=hJNiHdv29Yg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 1jFQ_1eflTI
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=1jFQ_1eflTI&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video O_zkowOXemY
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=O_zkowOXemY&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video gHzP7U_cXi4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=gHzP7U_cXi4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video QQg8DqHI-H4
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=QQg8DqHI-H4&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video gZQoll091dk
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=gZQoll091dk&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video c51fXrfHaXM
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=c51fXrfHaXM&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video W9H3AmfTons
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=W9H3AmfTons&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video BnSjP3F_0Zo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=BnSjP3F_0Zo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video t2NF4YIOp18
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=t2NF4YIOp18&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video DbNWpKGqavo
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=DbNWpKGqavo&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video mhtr5WkjRGs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=mhtr5WkjRGs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 6JQPQIdAGqs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=6JQPQIdAGqs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video tT6K-Gz1Uhs
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=tT6K-Gz1Uhs&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video QHYqsukgpXU
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=QHYqsukgpXU&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video awL-XpFQoQ8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=awL-XpFQoQ8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video b26wW8uko8U
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=b26wW8uko8U&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video LDyKvnhOgWU
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=LDyKvnhOgWU&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video O3A5rpDJGPg
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=O3A5rpDJGPg&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video ZDjt4gT_-jA
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=ZDjt4gT_-jA&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video pfQ8EH735ro
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=pfQ8EH735ro&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 3vTFS7LQOC8
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=3vTFS7LQOC8&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 3W18DQCDxwc
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=3W18DQCDxwc&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video BoRi_pgFrl0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=BoRi_pgFrl0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video GaMP2BmOXp0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=GaMP2BmOXp0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video 9NcTW3jdm1M
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=9NcTW3jdm1M&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
Getting video gezU_zLYDw0
<HttpError 403 when requesting https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=gezU_zLYDw0&maxResults=50&key=AIzaSyCjHJhGRa1FOnAgvTC1Rmnd8C7Zbzeswis&alt=json returned "The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.">
'''


for i in re.findall(pattern, text):
    clean.add(i[1])
    print(i[1])
    #print (f'Found on line %s: %s' % (i+1, match.group()))
        
with open(id + "clean", "a") as ff:
            json.dump(list(clean), ff)