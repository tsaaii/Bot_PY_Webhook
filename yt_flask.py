from flask import Flask, request, jsonify 
from youtube_transcript_api import YouTubeTranscriptApi
import json
import requests


app = Flask(__name__)
@app.route('/results/<string:keyword>')
def key_word(keyword):
    keyword=str(keyword)
    url='https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&maxResults=5&order=viewCount&key=AIzaSyD43Zc0hcBFG_mDoFDeHmJqZ0Yhiq_ZjA0'.format(keyword)
    x1=requests.get(url)
    x2=json.loads(x1.text)
    #print(x2)
    result={}
    result2={}
    l=[]
    for i in range(0,len(x2['items'])):
        key=list(x2['items'][i]['id'].items())[1][1]
        l=l+[key]
        result['number']=i+1
        result['link']='https://www.youtube.com/watch?v={}'.format(list(x2['items'][i]['id'].items())[1][1])
        result['channel title']=x2['items'][i]['snippet']['channelTitle']
        result['description']=x2['items'][i]['snippet']['description']
        result['upload date']=x2['items'][i]['snippet']['publishedAt']
        try:
            stir=''
            k=YouTubeTranscriptApi.get_transcript(l[i])
            for idx, val in enumerate(k):
                y=val['text']
                stir=stir+y
        except:
            stir='no subtitles found'
        resulti1={'parameters':{'link':result['link'],'channel title':result['channel title'],'description':result['description'],'video number':result['number'],'subtitles':stir,'uploaded on':result['upload date']}}
        result2[i]=resulti1['parameters']
        #print(result2)
    return jsonify(result2)
if __name__ == '__main__':
   app.config['JSON_AS_ASCII']=False
   app.run(debug=True,port=5000)
   
