#TwitterModule modified 2018/5/25
import sys
sys.path.append('../const')
from consts import TW_KEY
import json
from requests_oauthlib import OAuth1Session

CK = TW_KEY[0]
CS = TW_KEY[1]
AT = TW_KEY[2]
AS = TW_KEY[3]
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

def TweetPic(pic_path):
    twitter = OAuth1Session(CK, CS, AT, AS)

    files = {'media' : open(pic_path, 'rb')}
    req_media = twitter.post(url_media, files = files)

    if(req_media.status_code != 200):
        print('pic update fail')
        exit()

    media_id = json.loads(req_media.text)['media_id']

    params = {'status':'test', 'media_ids':[media_id]}
    req_media = twitter.post(url_text, params = params)

    if(req_media.status_code != 200):
        print('tweet update fail')
        exit()

    print('tweet')
    return 0
